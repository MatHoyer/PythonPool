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


def ft_invert(img):
    '''
    Takes a numpy array of an image (RGB)
    Return a numpy array of the inverted image
    '''
    return [255, 255, 255] - img


def ft_red(img):
    '''
    Takes a numpy array of an image (RGB)
    Return a numpy array of the red image
    '''
    return img * [1, 0, 0]


def ft_green(img):
    '''
    Takes a numpy array of an image (RGB)
    Return a numpy array of the green image
    '''
    for row in img:
        for pixels in row:
            pixels[0] = 0
            pixels[2] = 0
    return img


def ft_blue(img):
    '''
    Takes a numpy array of an image (RGB)
    Return a numpy array of the blue image
    '''
    for row in img:
        for pixels in row:
            pixels[0] = 0  # rouge
            pixels[1] = 0  # vert
    return img


def ft_grey(img):
    '''
    Takes a numpy array of an image (RGB)
    Return a numpy array of the grey image
    '''
    for row in img:
        for pixels in row:
            grey = pixels.max()
            # grey = (int)(pixels.sum() / 3)
            pixels[0] = grey
            pixels[1] = grey
            pixels[2] = grey
    return img


def main():
    '''
    Load an image, modify and display it
    '''
    img = ft_load("landscape.jpg")
    print(img)
    img = ft_invert(img)
    display(img)


if __name__ == '__main__':
    main()
