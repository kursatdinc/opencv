# CANNY EDGE DETECTION

import cv2 as cv
import numpy as np

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/keanu.jpeg")
cv.imshow("keanu" , src)
cv.waitKey(1)

edge = cv.Canny(src, 100, 300)
cv.imshow("edge", edge)
cv.waitKey(1)
