# implementation of pic shift

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

dst = np.zeros(info, np.uint8)

for i in range(height):
    for j in range(width - 100):
        dst[i, j + 100] = img[i, j]

cv2.imshow('dst', dst)
cv2.waitKey(0)