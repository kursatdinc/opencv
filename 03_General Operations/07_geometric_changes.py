# GEOMETRIC CHANGES

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "rocket.jpeg")

rows = img.shape[0]
cols = img.shape[1]

cv.imshow("original", img)
cv.waitKey(1)

# Shifting

M = np.float32([[1, 0, 300], [0, 1, 90]])

shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("shifted", shifted)
cv.waitKey(1)

# Rotation

M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

rotated = cv.warpAffine(img, M, (cols, rows))

cv.imshow("rotated", rotated)
cv.waitKey(1)

# Scaling

res = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)

cv.imshow("res", res)
cv.waitKey(1)