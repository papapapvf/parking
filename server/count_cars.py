import cv2
import numpy as np
import imutils
# from matplotlib import pyplot as plt

def imshow(img):
	cv2.imshow('img', img)
	cv2.waitKey(0)

img1 = cv2.imread('parking.jpg')
img2 = cv2.imread('background.jpg')

imshow(img2)
imshow(img1)

img1 = cv2.bilateralFilter(img1, 10, 75, 75)
img2 = cv2.bilateralFilter(img2, 10, 75, 75)

img = cv2.addWeighted(img1, 1, -img2, 1, 0)
img = cv2.bilateralFilter(img, 10, 75, 75)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel, iterations = 2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

imshow(sure_bg)

cnts = cv2.findContours(sure_bg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for c in cnts:
	if cv2.contourArea(c) > 3000:
		print cv2.contourArea(c)
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
	 
		cv2.drawContours(img1, [c], -1, (0, 255, 0), 2)

imshow(img1)

cv2.destroyAllWindows()