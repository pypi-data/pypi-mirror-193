# %%
from openprox import *
from openprox.utils import *
import openprox.utils.init.mosaic as moasic

import os
import cv2
import numpy as np
from scipy import ndimage
import hdf5storage

from openprox.utils.init.sr import shift_pixel


EPS = 1e-4


def filename(path):
    return os.path.basename(path)


def imread_uint(path, n_channels=3):
    #  input: path
    # output: HxWx3(RGB or GGG), or HxWx1 (G)
    if n_channels == 1:
        img = cv2.imread(path, 0)  # cv2.IMREAD_GRAYSCALE
        img = np.expand_dims(img, axis=2)  # HxWx1
    elif n_channels == 3:
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # BGR or G
        if img.ndim == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # GGG
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # RGB
    return img


def eval_dir(eval_single, root, gray=False):
    total_psnr = 0
    for i, name in enumerate(sorted(os.listdir(root))):
        path = os.path.join(root, name)
        I = imread_uint(path, 1 if gray else 3)

        psnr = eval_single(I)
        total_psnr += psnr
        print(i, filename(name), psnr, total_psnr / (i+1))
    return total_psnr / len(os.listdir(root))


def demosaic(I):
    hi = 49
    low = 0.6
    iter_num = 40

    CFA, CFA4, b, mask = moasic.mosaic_CFA_Bayer(I)

    y = np.float32(b) / 255

    M = Mosaic()
    x = Variable()

    data_term = sum_squares(M, y)
    deep_reg = deep_prior(x, denoiser='drunet_color', x8=True, clamp=True)  # x8 required
    problem = Problem(data_term+deep_reg)

    rhos, sigmas = log_descent(hi, low, iter_num)

    # input of drunet must be inited, otherwise, it fails
    x0 = moasic.dm_matlab(moasic.uint2tensor4(CFA4))

    x_pred = problem.solve(solver='hqs',
                           x0=x0,
                           weights={deep_reg: sigmas},
                           rhos=rhos,
                           max_iter=iter_num,
                           pbar=False)

    out = to_ndarray(x_pred.clamp(0, 1), debatch=True)
    out[mask] = y[mask]  # copy good pixel to out directly

    out = np.uint8((out*255).round())

    psnr_ = psnr(out, I, data_range=255)
    return psnr_


def deblur(I):
    # parameters
    
    noise_level_img = 7.65/255.0
    noise_level_model = noise_level_img

    hi = 49
    low = noise_level_model*255.
    iter_num = 8

    # prepare input
    
    kernels = hdf5storage.loadmat(os.path.join('kernels', 'Levin09.mat'))['kernels']

    k = kernels[0, 0].astype(np.float64)
    b = ndimage.filters.convolve(I, np.expand_dims(k, axis=2), mode='wrap')
    b = np.float32(b) / 255

    np.random.seed(seed=0)  # for reproducibility
    b += np.random.normal(0, noise_level_img, b.shape)  # add AWGN
    y = np.float32(b)
    
    # define problem
    
    D = Conv(k)
    x = Variable()

    data_term = sum_squares(D, y)
    deep_reg = deep_prior(x, denoiser='drunet_color', x8=True, clamp=False)  # x8 required
    problem = Problem(data_term+deep_reg)

    # solve

    rhos, sigmas = log_descent(hi, low, iter_num, sigma=noise_level_model)
    
    x0 = y

    x_pred = problem.solve(solver='hqs',
                           x0=x0,
                           weights={deep_reg: sigmas},
                           rhos=rhos,
                           max_iter=iter_num,
                           pbar=False)

    # compute psnr
    
    out = to_ndarray(x_pred.clamp(0, 1), debatch=True)
    out = np.uint8((out*255).round())

    psnr_ = psnr(out, I, data_range=255)
    return psnr_


def sr(I):
    # parameters
    
    noise_level_img = 0/255.0
    noise_level_model = noise_level_img
    sf = 2
    
    hi = 49
    low = max(sf, noise_level_model*255.)
    iter_num = 24

    # prepare input
    
    kernels = hdf5storage.loadmat(os.path.join('kernels', 'kernels_12.mat'))['kernels']

    k = kernels[0, 0].astype(np.float64)
    b = ndimage.filters.convolve(I, np.expand_dims(k, axis=2), mode='wrap')
    b = b[::sf, ::sf, ...]
    b = np.float32(b) / 255

    np.random.seed(seed=0)  # for reproducibility
    b += np.random.normal(0, noise_level_img, b.shape)  # add AWGN
    y = np.float32(b)
    
    
    # define problem
    
    x = Variable()
    data_term = sisr(x, k, sf, y)
    deep_reg = deep_prior(x, denoiser='drunet_color', x8=True, clamp=False)  # x8 required
    problem = Problem(data_term+deep_reg)

    
    # solve
    
    rhos, sigmas = log_descent(hi, low, iter_num)
    x0 = cv2.resize(b, (b.shape[1]*sf, b.shape[0]*sf), interpolation=cv2.INTER_CUBIC)
    x0 = shift_pixel(x0, sf)
    
    x_pred = problem.solve(solver='hqs',
                           x0=x0,
                           weights={deep_reg: sigmas},
                           rhos=rhos,
                           max_iter=iter_num,
                           pbar=False)

    # compute psnr
    
    out = to_ndarray(x_pred.clamp(0, 1), debatch=True)
    out = np.uint8((out*255).round())

    psnr_ = psnr(out, I, data_range=255)
    return psnr_


def test_demosaic():
    avg_psnr = eval_dir(demosaic, 'testsets/Kodak24', gray=False)
    print('avg=', avg_psnr)
    assert avg_psnr - 42.3679 < EPS, 'avg_psnr: {}'.format(avg_psnr)
    avg_psnr = eval_dir(demosaic, 'testsets/set3c', gray=False)
    assert avg_psnr - 40.2145 < EPS, 'avg_psnr: {}'.format(avg_psnr)


def test_deblur():
    avg_psnr = eval_dir(deblur, 'testsets/set3c', gray=False)
    assert avg_psnr - 29.2060 < EPS, 'avg_psnr: {}'.format(avg_psnr)


def test_sisr():
    avg_psnr = eval_dir(sr, 'testsets/set3c', gray=False)
    assert avg_psnr - 32.1499 < EPS, 'avg_psnr: {}'.format(avg_psnr)


if __name__ == '__main__':
    # test_deblur()
    # test_sisr()
    test_demosaic()
# %%
