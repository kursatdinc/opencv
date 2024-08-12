# IMAGE FLIP

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

img = cv.imread(path + "rocket.jpeg")

# X Flip

img_x_flip = cv.flip(img, 0)
cv.imshow("x-flip", img_flip)
cv.waitKey(1)

# Y Flip

img_y_flip = cv.flip(img, 1)
cv.imshow("y-flip", img_y_flip)
cv.waitKey(1)

# XY Flip

img_xy_flip = cv.flip(img, -1)
cv.imshow("xy-flip", img_xy_flip)
cv.waitKey(1)

cv.destroyAllWindows()