import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('parking.jpg')
img2 = cv2.imread('background.jpg')

img = cv2.addWeighted(img1, 1, -img2, 1, 0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

sure_bg = cv2.dilate(opening,kernel,iterations=3)

cv2.imshow('img', sure_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()