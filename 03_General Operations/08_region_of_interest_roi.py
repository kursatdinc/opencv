# ROI (REAGION OF INTEREST)

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "rocket.jpeg")

h, w = img.shape[:2]

src = img.copy()

roi = img[300:750, 950:1300, :]

cv.imshow("roi", roi)
cv.waitKey(1)