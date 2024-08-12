# HISTOGRAM EQUALIZATION

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    
    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align="center", color="r", alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel("Frequency")
    plt.xlabel("Histogram")
    plt.show()

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/scene-sample.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

custom_hist(gray)

dst = cv.equalizeHist(gray)
cv.imshow("eh", dst)
cv.waitKey(1)

custom_hist(dst)