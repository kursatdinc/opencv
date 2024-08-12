# QR CODE DETECT

import cv2 as cv
import numpy as np

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/qr-code.png")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

qr = cv.QRCodeDetector()

codeinfo, points, straight_qrcode = qr.detectAndDecode(gray)

print(points)

result = np.copy(src)

cv.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)

cv.imshow("qr_code", result)
cv.waitKey(1)

print(codeinfo)