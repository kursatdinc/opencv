# HOFFMAN LINE DETECTION

import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 250
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow("canny", canny_output)
    return canny_output

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/sudoku.jpeg")
cv.imshow("sudoku", src)
cv.waitKey(1)

binary = canny_demo(src)
cv.imshow("binary", binary)
cv.waitKey(1)

lines = cv.HoughLines(binary, 1, np.pi/180, 150, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

cv.imshow("hoffman", src)
cv.waitKey(1)
