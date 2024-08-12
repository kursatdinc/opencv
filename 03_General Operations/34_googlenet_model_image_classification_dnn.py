# IMAGE CLASSIFICATION DNN WITH GOOGLENET MODEL

# GoogleNet Modeline Ait Katmanların Bilgilerini Okuma

import cv2 as cv
import numpy as np

path = "/Users/krtdnc/Desktop/Miuul/OpenCV/"

bin_model = "/Users/krtdnc/Desktop/Miuul/OpenCV/models/bvlc_googlenet.caffemodel"
protxt = "/Users/krtdnc/Desktop/Miuul/OpenCV/models/bvlc_googlenet.prototxt"

net = cv.dnn.readNet(bin_model, protxt)

layer_names = net.getLayerNames()

for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name : %s" % (id, layer.type, layer.name))

# GoogleNet Modeli ile Görüntü Sınıflandırma

with open("/Users/krtdnc/Desktop/Miuul/OpenCV/imagenet-classes.txt", "rt") as f:
    classes = f.read().split("\n")

net = cv.dnn.readNet(protxt, bin_model)

image1 = cv.imread(path + "sax.jpeg")
image2 = cv.imread(path + "dog.jpg")

blob = cv.dnn.blobFromImage(image1, 1.0, (224, 224), (104, 117, 123), False, crop=False)

result = np.copy(image1)

net.setInput(blob)
out = net.forward()

out = out.flatten()

classId = np.argmax(out)

confidence = out[classId]

t, _ = net.getPerfProfile()
label = "cost time: %.2f ms" % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

label = "%s: %.4f" % (classes[classId] if classes else "Class #%d" % classId, confidence)
cv.putText(result, label, (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

show_img = np.hstack((image1, result))
cv.namedWindow("demo", cv.WINDOW_NORMAL)
cv.imshow("demo", show_img)
cv.waitKey(0)