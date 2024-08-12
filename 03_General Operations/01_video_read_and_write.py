# VIDEO READ AND WRITE

import cv2 as cv
import numpy as np

# READ

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

capture = cv.VideoCapture(path + "ds_path.mp4")

height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

# WRITE

out = cv.VideoWriter((path + "ds_path_save.avi"),
                     cv.VideoWriter_fourcc("D", "I", "V", "X"), 15,
                     (np.int_(width), np.int_(height)), True)

while True:
    # Kameradan Görüntü Al
    ret, frame = capture.read()

    # Görüntü Başarıyla Alındı mı Kontrol Et
    if ret is True:

        # Görüntüyü Oku
        cv.imshow("video-input", frame)
        out.write(frame)
        # 50sn sonra çık
        c = cv.waitKey(50)

        if c == 27:  # ESC
            break
   
    else:
        break

capture.release()
out.release()