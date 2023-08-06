from typing import List, Union

import torch

from dprox.proxfn import ProxFn

from .admm import ADMM, LinearizedADMM, ADMM_vxu
from .hqs import HQS
from .pc import PockChambolle
from .pgd import ProximalGradientDescent
from .base import Algorithm
from .opt import absorb

from .special import DEQSolver

SOLVERS = {
    'admm': ADMM,
    'admm_vxu': ADMM_vxu,
    'ladmm': LinearizedADMM,
    'hqs': HQS,
    'pc': PockChambolle,
    'pgd': ProximalGradientDescent,
}

SPECAILIZATIONS = {
    'deq': DEQSolver
}


def compile(prox_fns, method='admm', device='cuda', **kwargs):
    algorithm: Algorithm = SOLVERS[method]
    device = torch.device(device) if isinstance(device, str) else device

    psi_fns, omega_fns = algorithm.partition(prox_fns)
    solver = algorithm.create(psi_fns, omega_fns, **kwargs)
    solver = solver.to(device)
    return solver


def specialize(solver, method='deq', **kwargs):
    return SPECAILIZATIONS[method](solver, **kwargs)


class Problem:
    def __init__(
        self,
        prox_fns: Union[ProxFn, List[ProxFn]],
        absorb=True,
        merge=True,
        try_diagonalize=True,
        try_freq_diagonalize=True,
        lin_solver_kwargs={},
    ):
        if isinstance(prox_fns, ProxFn):
            prox_fns = [prox_fns]
        self.prox_fns = prox_fns

        self.absorb = absorb
        self.merge = merge

        self.solver_args = dict(
            try_diagonalize=try_diagonalize,
            try_freq_diagonalize=try_freq_diagonalize,
            lin_solver_kwargs=lin_solver_kwargs,
        )

    @property
    def objective(self):
        return self.prox_fns

    def optimize(self):
        if self.absorb:
            self.prox_fns = absorb.absorb_all_lin_ops(self.prox_fns)
        if self.merge:
            self.prox_fns = merge.merge_all(self.prox_fns)

    def solve(self, method='admm', device='cuda', **kwargs):
        solver = compile(self.prox_fns, method=method, device=device, **self.solver_args)
        results = solver.solve(**kwargs)
        return results

    def visuliaze(self, savepath):
        pass
