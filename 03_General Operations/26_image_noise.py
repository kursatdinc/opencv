# IMAGE NOISE

import cv2 as cv
import numpy as np

src = cv.imread("/Users/krtdnc/Desktop/Miuul/OpenCV/cry-woman.png")
cv.imshow("original", src)
cv.waitKey(1)

h, w = src.shape[:2]
copy = np.copy(src)

# salt-pepper noise
def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 100000
    rows = np.random.randint(0, h, nums, dtype=np.int_)
    cols = np.random.randint(0, w, nums, dtype=np.int_)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image

spn = add_salt_pepper_noise(copy)
cv.imshow("spn", spn)
cv.waitKey(1)