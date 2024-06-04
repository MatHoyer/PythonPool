import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    '''
    Takes a path to an image
    Return the image as a numpy array (RGB)
    '''
    try:
        if type(path) is not str:
            raise ValueError('path is not a string')
        with Image.open(path) as img:
            array = np.array(img)

        print('The shape of the image is : ', array.shape)
        
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)
    return array
