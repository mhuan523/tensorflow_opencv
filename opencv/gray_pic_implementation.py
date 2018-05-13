# implementation of gray pic

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
        #gray = np.uint8((int(b) + int(g) + int(r)) / 3)
        b = int(b)
        g = int(g)
        r = int(r)
        #gray = b * 0.299 + g * 0.587 + r * 0.114
        gray = (b + (g << 1) + r) >> 2
        dst[i, j] = np.uint8(gray)

cv2.imshow('dst', dst)
cv2.waitKey(0)