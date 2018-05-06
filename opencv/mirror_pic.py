# implementation of mirror pic

import cv2
import numpy as np

img = cv2.imread('../picture/mountain.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]

dstInfo = (height * 2, width, mode)
dst = np.zeros(dstInfo, np.uint8)

for i in range(height):
    for j in range(width):
        # dst[i, j] = img[i, j]
        # dst[2 * height - i - 1, j] = img[i, j]
        dst[height + i, j] = img[i, j]
        dst[height - i, j] = img[i, j]

for i in range(width):
    dst[height, i] = (0, 0, 255)

cv2.imwrite('../picture/mountain_mirror.jpg', dst)
