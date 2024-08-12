# GRAY IMAGE

import cv2 as cv

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

img = cv.imread(path + "rocket.jpeg")

#cvtColor

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img_gray)
cv.waitKey(1)

#imwrite

cv.imwrite("/Users/krtdnc/Desktop/Miuul/OpenCV/01_Basic Operations/rocket_gray.jpeg", img_gray)

cv.destroyAllWindows()

# img = cv.imread(path + "rocket.jpeg", cv.IMREAD_GRAYSCALE) de kullanılabilir.