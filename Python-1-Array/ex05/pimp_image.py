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
		for pixel in row:
			pixel[0] = 0 #rouge
			pixel[1] = 0 #vert
	return img

def ft_grey(img):
	for row in img:
		for pixel in row:
			median = (pixel[0] + pixel[1] + pixel[2]) / 3
			pixel[0] = median
			pixel[1] = median
			pixel[2] = median
	return img
	
def main():
	img = ft_load("landscape.jpg")
	print(img)
	img = ft_grey(img)
	display(img)

if __name__ == '__main__':
	main()