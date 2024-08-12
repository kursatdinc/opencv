# MERGING TWO IMAGES

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img1 = cv.imread(path + "rocket.jpeg")
img2 = cv.imread(path + "rocket_gray.jpeg")

horizontal = np.hstack((img1, img2))

cv.imshow("merge_img", horizontal)
cv.waitKey(1)

cv.destroyAllWindows()