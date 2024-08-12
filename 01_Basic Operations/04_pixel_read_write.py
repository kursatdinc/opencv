# PIXEL READ WRITE

# Resim Inverse Almak

import cv2 as cv

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"
img = cv.imread(path + "open-cv.png")
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

h, w, ch = img.shape
print("h, w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = (b, g, r)


cv.imshow("output", img)
cv.waitKey(1)

cv.destroyAllWindows()