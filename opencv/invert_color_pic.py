# invert color pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

colorDst = np.zeros(info, np.uint8)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range(height):
    for j in range(width):
        dst[i, j] = 255 - dst[i, j]
        colorDst[i, j] = (255 - img[i, j][0], 255 - img[i, j][1], 255 - img[i, j][2])

cv2.imshow('dst', dst)
cv2.imshow('colorDst', colorDst)
cv2.waitKey(0)