# IMAGE PIXEL NORMALIZATION

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "rocket.jpeg")

print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

print(gray.shape)

gray = np.float32(gray)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min_loc:", min_loc, ",", "max_loc:", max_loc)

means, stddev = cv.meanStdDev(gray)
print("means: %.2f, stddev: %.2f" % (means, stddev))

# NORM_MINMAX

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

means, stddev = cv.meanStdDev(dst)
print("means: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)

# NORM_INF

dst2 = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst2, alpha=0, beta=1.0, norm_type=cv.NORM_INF)
print(dst2)

means, stddev = cv.meanStdDev(dst2)
print("means: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_INF", dst2)
cv.waitKey(1)

# NORM_L1

dst3 = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst3, alpha=0, beta=1.0, norm_type=cv.NORM_L1)
print(dst3)

means, stddev = cv.meanStdDev(dst3)
print("means: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_INF", dst3)
cv.waitKey(1)

# NORM_L2

dst4 = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst4, alpha=0, beta=1.0, norm_type=cv.NORM_L1)
print(dst4)

means, stddev = cv.meanStdDev(dst4)
print("means: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_INF", dst4)
cv.waitKey(1)