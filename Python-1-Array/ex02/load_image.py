import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    with Image.open(path) as img:
        array = np.array(img)

    print('The shape of the image is : ', array.shape)
    return array
