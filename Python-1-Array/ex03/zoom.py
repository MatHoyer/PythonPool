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


def zoom(img: np.array, zoomFactor=2):
    '''
    Takes a numpy array of an image (RGB) and a zoom factor
    Return a numpy array of the zoomed image
    '''
    try:
      if type(img) is not np.array:
          raise ValueError('img is not a numpy array')
      if type(zoomFactor) is not int or zoomFactor <= 0:
          raise ValueError('zoomFactor is not an positiv integer')
      
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

    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)

    return zoomedImg


def main():
    '''
    Load an image, zoom in and display it
    '''
    img = ft_load("animal.jpeg")
    print(img)
    img = zoom(img)
    display(img)


if __name__ == '__main__':
    main()
