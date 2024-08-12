# BASIC THRESHOLDING

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "rocket.jpeg")

T = 127

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)

cv.waitKey(1)