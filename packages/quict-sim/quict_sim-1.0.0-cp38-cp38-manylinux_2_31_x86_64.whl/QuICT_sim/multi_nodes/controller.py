from enum import Enum
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, as_completed

import cupy as cp
import numpy as np
from cupy.cuda import nccl

from QuICT.core import Circuit
from QuICT.ops.linalg.gpu_calculator import VectorPermutation

from QuICT_sim.proxy import Proxy
from QuICT_sim.multi_nodes import Transpile, MultiNodesSimulator


if mp.get_start_method(allow_none=True) != "spawn":
    mp.set_start_method("spawn", force=True)


class DeviceType(Enum):
    cpu = "CPU",
    gpu = "GPU"


class ModeType(Enum):
    local = "local"
    distributed = "distributed"


def worker(circuit, ndev, uid, dev_id, precision, device: str = "GPU"):
    proxy = Proxy(ndevs=ndev, uid=uid, dev_id=dev_id)
    simulator = MultiNodesSimulator(
        proxy=proxy,
        device=device,
        gpu_device_id=dev_id,
        precision=precision
    )
    state = simulator.run(circuit)

    return dev_id, state


class MultiNodesController:
    # Not support noise circuit
    def __init__(
        self,
        ndev: int,
        dev_type: DeviceType = DeviceType.gpu,
        mode: ModeType = ModeType.local,
        precision: str = "double",
    ):
        self.ndev = ndev
        self._device_type = dev_type
        self._mode_type = mode
        self._precision = precision

        self._transpiler = Transpile(self.ndev)

    def run(self, circuit: Circuit):
        # transpile circuit
        divided_circuits, split_qubit = self._transpiler.run(circuit)

        # Prepare mapping permutation
        inner_mapping = list(range(circuit.width()))
        inner_mapping.remove(int(split_qubit))
        permutation = [split_qubit] + inner_mapping

        # start launch multi-node simulator
        if self._mode_type == ModeType.local:
            return self._launch_local(divided_circuits, permutation)

    def _launch_local(self, dcircuit: Circuit, permutation: list):
        # Using multiprocess to start simulators, only for GPUs
        proxy_id = nccl.get_unique_id()
        with ProcessPoolExecutor(max_workers=self.ndev) as executor:
            tasks = [
                executor.submit(
                    worker,
                    dcircuit,
                    self.ndev,
                    proxy_id,
                    dev_id,
                    self._precision
                ) for dev_id in range(self.ndev)
            ]

        results = []
        for t in as_completed(tasks):
            results.append(t.result())

        z = [None] * self.ndev
        for idx, vec in results:
            z[idx] = vec

        combined_sv = cp.concatenate(z)
        return VectorPermutation(combined_sv, np.array(permutation))

    def _launch_distributed(self):
        # send job to distributed
        pass
