import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes a list, a start index and an end index
    Return a list that contains the elements between the start and end index
    '''
    try:
        if type(family) is not list:
            raise ValueError('The family should be a list')
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
