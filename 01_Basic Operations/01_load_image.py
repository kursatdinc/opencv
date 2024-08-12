# LOAD IMAGE

import cv2 as cv

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

img = cv.imread(path + "rocket.jpeg")

type(img)

# namedWindow
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

# imshow
cv.imshow("opencv_test", img)
cv.waitKey(1)

cv.destroyAllWindows()