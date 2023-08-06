import imageio
import numpy as np

from . import to_ndarray


def imread_rgb(path):
    """
    Read an image from a file.
    """
    from PIL import Image
    import numpy as np
    img = Image.open(path)
    return np.asarray(img)


def imshow(*imgs, maxcol=3, gray=False):
    import matplotlib.pyplot as plt
    if len(imgs) != 1:
        plt.figure(figsize=(10, 5))
    row = (len(imgs) - 1) // maxcol + 1
    col = maxcol if len(imgs) >= maxcol else len(imgs)
    for idx, img in enumerate(imgs):
        img = to_ndarray(img, debatch=True)
        if img.max() > 2: img = img / 255
        img = img.clip(0, 1)
        if gray or len(img.shape) == 2: plt.gray()
        plt.subplot(row, col, idx + 1)
        plt.imshow(img)
    plt.show()


def imread(path):
    img = imageio.imread(path)
    return np.float32(img) / 255


def filter_ckpt(prefix, ckpt, remove_prefix=True):
    new_ckpt = {}
    for k, v in ckpt.items():
        if k.startswith(prefix):
            if remove_prefix: new_k = k.replace(prefix, '')
            else: new_k = k
            new_ckpt[new_k] = v
    return new_ckpt
