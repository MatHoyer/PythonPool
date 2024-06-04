from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.array):
    '''
    Takes a numpy array of an image (RGB)
    Display the image
    '''
    plt.imshow(array)
    plt.show()


def rotate_matrix_90(mat: np.array):
    num_rows = len(mat)
    num_cols = len(mat[0])
    result = [[0]*num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][num_rows-1-i] = mat[i][j]
    return np.array(result)


def mirror_effect(mat: np.array):
    return mat[:, ::-1]


def rotate(img: np.array, angle=90):
    '''
    Takes a numpy array of an image (RGB) and an angle
    Return a numpy array of the rotated image
    '''
    img = rotate_matrix_90(img)
    img = mirror_effect(img)
    return img


def main():
    '''
    Load an image, rotate and display it
    '''
    img = ft_load("animal.jpeg")
    print(img)
    img = rotate(img)
    display(img)


if __name__ == '__main__':
    main()
