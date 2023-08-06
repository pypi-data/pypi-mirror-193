import os
import copy
from os.path import join

import torch
import torch.nn as nn

from ..base import ProxFn
from .denoisers import (DRUNetDenoiser, FFDNetColorDenoiser, FFDNetDenoiser,
                        GRUNetDenoiser, IRCNNDenoiser, UNetDenoiser)
from .denoisers.base import Denoiser
from .denoisers.composite import Augment

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_denoiser(type):
    if type == 'ffdnet':
        model_path = join(CURRENT_DIR, 'model_zoo/ffdnet_gray.pth')
        return FFDNetDenoiser(model_path)
    if type == 'ffdnet_color':
        model_path = join(CURRENT_DIR, 'model_zoo/ffdnet_color.pth')
        return FFDNetColorDenoiser(model_path)
    if type == 'drunet_color':
        model_path = join(CURRENT_DIR, 'model_zoo/drunet_color.pth')
        return DRUNetDenoiser(3, model_path)
    if type == 'drunet':
        model_path = join(CURRENT_DIR, 'model_zoo/drunet_gray.pth')
        return DRUNetDenoiser(1, model_path)
    if type == 'ircnn':
        model_path = join(CURRENT_DIR, 'model_zoo/ircnn_gray.pth')
        return IRCNNDenoiser(1, model_path)
    if type == 'grunet':
        model_path = join(CURRENT_DIR, 'model_zoo/unet_qrnn3d.pth')
        return GRUNetDenoiser(model_path)
    if type == 'unet':
        model_path = join(CURRENT_DIR, 'model_zoo/unet-nm.pt')
        return UNetDenoiser(model_path)


def clone(x, nums, shared):
    return [x if shared else copy.deepcopy(x) for _ in range(nums)]


class deep_prior(ProxFn):
    def __init__(self, linop, denoiser='ffdnet', x8=False, clamp=False, trainable=False, unroll_step=None, sqrt=True):
        super().__init__(linop)
        self.name = denoiser

        if isinstance(denoiser, str):
            self.denoiser = get_denoiser(denoiser)
        else:
            self.denoiser = denoiser

        self.x8 = x8
        self.clamp = clamp
        self.sqrt = sqrt
        if x8:
            self.denoiser = Augment(self.denoiser)

        if not trainable:
            self.denoiser.eval()
            self.denoiser.requires_grad_(False)

        self.unroll = unroll_step is not None
        if unroll_step is not None:
            self.denoisers = nn.ModuleList(clone(self.denoiser, unroll_step, shared=False))

    def _reload(self, shape=None):
        if self.x8:
            self.denoiser.reset()

    def eval(self, v):
        raise NotImplementedError('deep prior cannot be explictly evaluated')

    def _prox(self, v: torch.Tensor, lam: torch.Tensor):
        """ v: [N, C, H, W]
            lam: [1]
        """
        if self.sqrt: lam = lam.sqrt()
        if self.clamp: v = v.clamp(0, 1)
        if torch.is_complex(v): v = v.real
        if self.unroll: out = self.denoisers[self.step].denoise(v, lam)
        else: out = self.denoiser.denoise(v, lam)
        return out.type_as(v)

    def __repr__(self):
        return f'deep_prior(denoiser="{self.name}")'
