from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def display(array: np.array):
	plt.imshow(array)
	plt.show()

def rotate(img, angle=90):
	height = img.shape[0]
	width = img.shape[1]

	img = np.rot90(img, k=angle//90)
	return img

def main():
	img = ft_load("animal.jpeg")
	print(img)
	img = rotate(img, 180)
	display(img)

if __name__ == '__main__':
	main()