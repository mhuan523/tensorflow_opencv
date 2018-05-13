# mosaic pic with opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

for i in range(100, 200):
    for j in range(100, 200):
        if i % 10 == 0 and j % 10 == 0:
            for m in range(10):
                for n in range(10):
                    img[i + m, j + n] = img[i, j]

cv2.imshow('dst', img)
cv2.waitKey(0)