# HOFFMAN CIRCLE DETECTION

import cv2 as cv
import numpy as np

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/coins.jpeg")
cv.imshow("coins", src)
cv.waitKey(1)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=10, param1=150, param2=50, minRadius=20, maxRadius=100)

for c in circles[0, :]:
    print(c)
    cx, cy, r = c
    cv.circle(src, (int(cx), int(cy)), 2, (0, 255, 0), 2, 8, 0)
    cv.circle(src, (int(cx), int(cy)), int(r), (0, 0, 255), 2, 8, 0)

cv.imshow("hough circle demo", src)
cv.waitKey(1)