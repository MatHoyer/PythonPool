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


def rotate(img, angle=90):
    '''
    Takes a numpy array of an image (RGB) and an angle
    Return a numpy array of the rotated image
    '''
    img = np.rot90(img, k=angle//90)
    return img


def main():
    '''
    Load an image, rotate and display it
    '''
    img = ft_load("animal.jpeg")
    print(img)
    img = rotate(img, 180)
    display(img)


if __name__ == '__main__':
    main()
