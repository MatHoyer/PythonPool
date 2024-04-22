from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def display(array: np.array):
	plt.imshow(array)
	plt.show()

def zoom(img, zoomFactor=2):
	height = img.shape[0]
	width = img.shape[1]

	# Find the point to zoom in on (here is the center of the image)
	centerY = height // 2
	centerX = width // 2

	# Determine the size of the zoomed region
	zoomHeight = height // zoomFactor
	zoomWidth = width // zoomFactor

	# Find the region to zoom in on (coordinates of the top-left and bot-right corner of the region)
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