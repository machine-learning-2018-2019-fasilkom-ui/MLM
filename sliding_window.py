# USAGE
# python sliding_window.py --image images/adrian_florida.jpg 

# import the necessary packages
import argparse
import time
import cv2

#slider
def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


def run_slide(image_dir):
	list_imgs = list()
	list_coors = list()
	image = cv2.imread(image_dir)
	(winW, winH) = (64, 64)

	for (x, y, window) in sliding_window(image, stepSize=32, windowSize=(winW, winH)):
		# if the window does not meet our desired window size, ignore it
		if window.shape[0] != winH or window.shape[1] != winW:
			continue
			#----------------------crop_img bagian yang di highlight/diambil
		crop_img = image[y:y+winH, x:x+winW]
		list_imgs.append(crop_im)
		list_coors.append((x,y))
	return (list_imgs, list_coors)
	