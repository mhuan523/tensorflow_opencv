# lighten pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

dst = np.zeros(info, np.uint8)

for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        bb = b * 1.3
        if bb > 255:
            b = 255
        gg = g * 1.2
        if gg > 255:
            bb = 255
        dst[i, j] = (bb, gg, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)
