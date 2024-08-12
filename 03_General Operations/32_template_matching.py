# TEMPLATE MATCHING

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

def template_demo():
    src = cv.imread(path + "/open-cv.png")
    tpl = cv.imread(path + "/open-cv-test.png")

    cv.imshow("input", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, tpl, method=cv.TM_CCORR_NORMED)
    cv.imshow("result", result)

    # cv.imwrite(path + "/result.png", np.uint8(result*255))
    t = 0.85
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)

    cv.imshow("ilk_demo", src)

template_demo()
cv.waitKey(1)