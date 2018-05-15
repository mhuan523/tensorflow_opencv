# implementation of mean filter of pic

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

dst = np.zeros(info, np.uint8)

for i in range(3, height - 3):
    for j in range(3, width - 3):
        sum_b, sum_g, sum_r = 0, 0, 0
        (b, g, r) = img[i, j]
        for m in range(-3, 3):
            for n in range(-3, 3):
                sum_b = sum_b + img[i + m, j + n][0]
                sum_g = sum_g + img[i + m, j + n][1]
                sum_r = sum_r + img[i + m, j + n][2]
        dst[i, j] = (np.uint8(sum_b / 36), np.uint8(sum_g / 36), np.uint8(sum_r / 36))

cv2.imshow('dst', dst)
cv2.waitKey(0)
