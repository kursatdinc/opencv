# IMAGE PIXEL VALUE STATISTICS

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "rocket.jpeg", cv.IMREAD_GRAYSCALE)

# minMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(img)

print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min_loc:", min_loc, ",", "max_loc:", max_loc)

# meanStdDev

means, stddev = cv.meanStdDev(img)

print("means: %.2f, stddev: %.2f" % (means, stddev))

# Resmin pixel ortalamasından büyük/küçüklere göre filtrelemek

img[np.where(img < means)] = 0
img[np.where(img > means)] = 255

cv.imshow("img", img)
cv.waitKey(1)

cv.destroyAllWindows()