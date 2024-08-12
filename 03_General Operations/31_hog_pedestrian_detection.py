# HOG (Histogram of Oriented Gradients) PEDESTRIAN DETECTION

import cv2 as cv

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/pedestrian.jpeg")

hog = cv.HOGDescriptor()

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.25)


for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("hog_pedestrian", src)
cv.waitKey(1)