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

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and define the window width and height
image = cv2.imread(args["image"])
(winW, winH) = (64, 64)

for (x, y, window) in sliding_window(image, stepSize=32, windowSize=(winW, winH)):
	# if the window does not meet our desired window size, ignore it
	if window.shape[0] != winH or window.shape[1] != winW:
		continue
	
	# since we do not have a classifier, we'll just draw the window
	clone = image.copy()
	
	#----------------------crop_img bagian yang di highlight/diambil
	crop_img = clone[y:y+winH, x:x+winW]
	#----------------------------------------------------

	cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
	cv2.imshow("Window", clone)


	
	cv2.waitKey(1)
	time.sleep(0.025)
	