# implementation of resize pic

import numpy as np
import cv2

img = cv2.imread('../picture/mountain.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]

dstHeight = int(height / 2)
dstWidth = int(width / 2)
dst = np.zeros((dstHeight, dstWidth, mode), np.uint8)

for i in range(dstHeight):
    for j in range(dstWidth):
        iNew = int(i * (height * 1.0 / dstHeight))
        jNew = int(j * (width * 1.0 / dstWidth))
        dst[i, j] = img[iNew, jNew]

cv2.imshow('dst', dst)
cv2.imwrite('../picture/mountain_resize.jpg', dst)
cv2.waitKey(0)