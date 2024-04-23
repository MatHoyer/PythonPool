import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        start = abs(int(start))
        end = abs(int(end))
        array = np.array(family)

        print(f'My shape is : {array.shape}')
        sliced_array = array[start:end]
        print(f'My new shape is : {sliced_array.shape}')
        return (sliced_array)
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)
