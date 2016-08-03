import cv2
import numpy as np
import imutils

def imshow(img):
	cv2.imshow('img', img)
	cv2.waitKey(0)

def get_cars(im1, im2):

	img1 = cv2.imread(im1)
	img2 = cv2.imread(im2)

	img1 = cv2.bilateralFilter(img1, 10, 75, 75)
	img2 = cv2.bilateralFilter(img2, 10, 75, 75)

	img = cv2.addWeighted(img1, 1, -img2, 1, 0)
	img = cv2.bilateralFilter(img, 10, 75, 75)

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	kernel = np.ones((3, 3), np.uint8)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel, iterations = 2)

	sure_bg = cv2.dilate(opening, kernel, iterations=3)

	cnts = cv2.findContours(sure_bg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	return filter(lambda c: cv2.contourArea(c) > 3000, cnts)

def main():
	import sys
	
	img1 = cv2.imread(sys.argv[1])

	for c in get_cars(sys.argv[1], sys.argv[2]):
		cv2.drawContours(img1, [c], -1, (0, 255, 0), 2)

	imshow(img1)
	cv2.destroyAllWindows()


if __name__ == '__main__':	
	main()