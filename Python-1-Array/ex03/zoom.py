from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.array):
    plt.imshow(array)
    plt.show()


def zoom(img, zoomFactor=2):
    height = img.shape[0]
    width = img.shape[1]

    centerY = height // 2
    centerX = width // 2

    zoomHeight = height // zoomFactor
    zoomWidth = width // zoomFactor

    startY = centerY - zoomHeight // 2
    startX = centerX - zoomWidth // 2
    endY = centerY + zoomHeight // 2
    endX = centerX + zoomWidth // 2

    zoomedImg = img[startY:endY, startX:endX]

    print('The shape of the zoomed image is : ', zoomedImg.shape)
    print(zoomedImg)

    return zoomedImg


def main():
    img = ft_load("animal.jpeg")
    print(img)
    img = zoom(img)
    display(img)


if __name__ == '__main__':
    main()
