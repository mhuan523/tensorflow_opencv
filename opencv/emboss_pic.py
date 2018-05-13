# emboss pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = np.zeros((height, width, 1), np.uint8)

for i in range(height):
    for j in range(width - 1):
        #dst[i, j] = np.uint8(int(gray[i, j]) - int(gray[i, j + 1]) + 150)
        dst[i, j] = int(gray[i, j]) - int(gray[i, j + 1]) + 150
        if dst[i, j] > 255:
            dst[i, j] = 255
        if dst[i, j] < 0:
            dst[i, j] = 0

cv2.imshow('dst', dst)
cv2.waitKey(0)
