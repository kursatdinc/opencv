# HARRIS CORNER DETECTION

import cv2 as cv
import numpy as np

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/chess.jpeg")
cv.imshow("original", src)
cv.waitKey(1)

def harris(image):
    blockSize = 2
    apertureSize = 3
    k = 0.04

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)
    
    return image

result = harris(src)
cv.imshow("result", result)
cv.waitKey(1)