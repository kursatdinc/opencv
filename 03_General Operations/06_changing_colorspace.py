# CHANGING COLORSPACE

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

# HSV

img = cv.imread(path + "rocket.jpeg")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(1)

# GRAY

img = cv.imread(path + "rocket.jpeg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)