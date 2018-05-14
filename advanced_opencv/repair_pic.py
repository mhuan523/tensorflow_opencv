# equalize hist of gray pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

for i in range(200, 300):
    img[i, 200 - 1] = (255, 255, 255)
    img[i, 200] = (255, 255, 255)
    img[i, 200 + 1] = (255, 255, 255)

for j in range(150, 250):
    img[250 - 1, j] = (255, 255, 255)
    img[250, j] = (255, 255, 255)
    img[250 + 1, j] = (255, 255, 255)

cv2.imshow('src', img)

paint = np.zeros((height, width, 1), np.uint8)

for i in range(200, 300):
    paint[i, 200 - 1] = 255
    paint[i, 200] = 255
    paint[i, 200 + 1] = 255

for j in range(150, 250):
    paint[250 - 1, j] = 255
    paint[250, j] = 255
    paint[250 + 1, j] = 255

dst = cv2.inpaint(img, paint, 3, cv2.INPAINT_TELEA)

cv2.imshow('dst', dst)
cv2.waitKey(0)