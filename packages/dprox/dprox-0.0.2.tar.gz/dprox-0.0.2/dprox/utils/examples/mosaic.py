import numpy as np

from .. import to_torch_tensor, to_ndarray


def masks_CFA_Bayer(shape):
    pattern = 'RGGB'
    channels = dict((channel, np.zeros(shape)) for channel in 'RGB')
    for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
        channels[channel][y::2, x::2] = 1
    return tuple(channels[c].astype(bool) for c in 'RGB')


def mosaicing(img):
    device = img.device
    img = to_ndarray(img, debatch=True)
    shape = img.shape[:2]
    R_m, G_m, B_m = masks_CFA_Bayer(shape)
    mask = np.concatenate((R_m[..., None], G_m[..., None], B_m[..., None]), axis=-1)
    b = mask * img
    b = to_torch_tensor(b, batch=True).to(device)
    return b


def mosaicing_np(img):
    shape = img.shape[:2]
    R_m, G_m, B_m = masks_CFA_Bayer(shape)
    mask = np.concatenate((R_m[..., None], G_m[..., None], B_m[..., None]), axis=-1)
    b = mask * img
    return b
