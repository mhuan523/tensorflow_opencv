# woolen glass pic with opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

for i in range(height - 8):
    for j in range(width - 8):
        position = int(np.random.random() * 8)
        img[i, j] = img[i + position, j + position]

cv2.imshow('dst', img)
cv2.waitKey(0)