import scipy.misc
import scipy.ndimage
import numpy as np
import cv2

from .. import to_torch_tensor, to_ndarray

samples = {
    'face': scipy.misc.face(),
    'ascent': scipy.misc.ascent(),
}


def sample(name='face', return_tensor=True):
    s = samples[name].copy().astype('float32') / 255
    if return_tensor:
        s = to_torch_tensor(s, batch=True).float()
    return s


def point_spread_function(ksize, sigma):
    return np.expand_dims(fspecial_gaussian(ksize, sigma), axis=2).astype('float32')


def blurring(img, psf):
    device = img.device
    img = to_ndarray(img, debatch=True)
    psf = to_ndarray(psf)
    b = scipy.ndimage.filters.convolve(img, psf, mode='wrap')
    b = to_torch_tensor(b, batch=True).to(device)
    return b


def fspecial_gaussian(hsize, sigma):
    hsize = [hsize, hsize]
    siz = [(hsize[0] - 1.0) / 2.0, (hsize[1] - 1.0) / 2.0]
    std = sigma
    [x, y] = np.meshgrid(np.arange(-siz[1], siz[1] + 1), np.arange(-siz[0], siz[0] + 1))
    arg = -(x * x + y * y) / (2 * std * std)
    h = np.exp(arg)
    h[h < scipy.finfo(float).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h = h / sumh
    return h


def downsampling(img, psf, sf):
    device = img.device
    img = to_ndarray(img, debatch=True)
    psf = to_ndarray(psf)
    blurred = scipy.ndimage.filters.convolve(img, psf, mode='wrap')
    downed = blurred[0::sf, 0::sf, ...]
    x0 = cv2.resize(downed, (downed.shape[1] * sf, downed.shape[0] * sf), interpolation=cv2.INTER_CUBIC)
    
    x0 = to_torch_tensor(x0, batch=True).to(device).float()
    downed = to_torch_tensor(downed, batch=True).to(device).float()
    return downed, x0
