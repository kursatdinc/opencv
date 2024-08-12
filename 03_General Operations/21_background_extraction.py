# BACKGROUND EXTRACTION

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("/Users/krtdnc/Desktop/Miuul/OpenCV/ds_path.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=100)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv.imshow("frame", frame)
    cv.imshow("fgmask", fgmask)
    cv.imshow("background", background)
    c = cv.waitKey(10)&0xff
    if c == 27:
        break

cap.release()