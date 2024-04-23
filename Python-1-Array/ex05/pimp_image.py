from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.array):
    plt.imshow(array)
    plt.show()


def ft_invert(img):
    return [255, 255, 255] - img


def ft_red(img):
    return img * [1, 0, 0]


def ft_green(img):
    return img - [255, 0, 255]


def ft_blue(img):
    for row in img:
        for pixels in row:
            pixels[0] = 0  # rouge
            pixels[1] = 0  # vert
    return img


def ft_grey(img):
    for row in img:
        for pixels in row:
            grey = pixels.max()
            # grey = (int)(pixels.sum() / 3)
            pixels[0] = grey
            pixels[1] = grey
            pixels[2] = grey
    return img


def main():
    img = ft_load("landscape.jpg")
    print(img)
    img = ft_grey(img)
    display(img)


if __name__ == '__main__':
    main()
