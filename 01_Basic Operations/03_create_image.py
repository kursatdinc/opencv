# CREATE IMAGE

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

img = cv.imread(path + "rocket.jpeg")
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)
cv.imshow("opencv_test", img)
cv.waitKey(1)

m1 = np.copy(img)

m2 = img

type(img)

img[100:200, 200:300, :] = 255

cv.imshow("m2", m2)
cv.waitKey(1)

# Resimle aynı boyutta sıfırlar oluşturmak

m3 = np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1)

# Gri resim oluşturmak

m4 = np.zeros([512, 512], np.uint8)
m4[:, :] = 127
cv.imshow("m4", m4)
cv.waitKey(1)

# Özel şekil çizmek

m5 = np.ones((550, 770, 3))
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)

cv.rectangle(m5, (480, 250), (100, 450), black, 8)
cv.rectangle(m5, (580, 150), (200, 350), black, 8)
cv.line(m5, (100, 450), (200, 350), black, 8)
cv.line(m5, (480, 250), (580, 150), black, 8)
cv.line(m5, (100, 250), (200, 150), black, 8)
cv.line(m5, (480, 450), (580, 350), black, 8)

start_point = (150, 100)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(m5, "ilk resim denemem", start_point, font, font_size, black, font_thickness)
cv.imshow("dikdörtgen", m5)
cv.waitKey(1)

cv.destroyAllWindows()