# change color of pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

dst = np.zeros((height, width, 3), np.uint8)

for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        b = (1.5 * b)
        if b > 255:
            b = 255
        g = (1.3 * g)
        if g > 255:
            g = 255
        dst[i, j] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)
