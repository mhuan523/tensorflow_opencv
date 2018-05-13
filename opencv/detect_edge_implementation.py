# implementation of detecting edge

import cv2
import numpy as np
import math

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = np.zeros((height, width, 1), np.uint8)

for i in range(height - 2):
    for j in range(width - 2):
        x = img[i, j] + img[i, j + 1] * 2 + img[i, j + 2] - \
            img[i + 2, j] - img[i + 2, j + 2] * 2 - img[i + 2, j + 2]
        y = img[i, j] + img[i + 1, j] * 2 + img[i + 2, j] - \
            img[i, j] - img[i + 1, j + 1] * 2 - img[i + 2, j + 2]
        value = math.sqrt(x * x + y * y)
        if value > 50:
            dst[i, j] = 255
        else:
            dst[i, j] = 0

cv2.imshow('dst', dst)
cv2.waitKey(0)
