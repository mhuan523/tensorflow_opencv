# implementation of median filter of pic

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = np.zeros((height, width, 1), np.uint8)
collect = np.zeros(9, np.uint8)

for i in range(1, height - 1):
    for j in range(1, width - 1):
        k = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                collect[k] = gray[i + m, j + n]
                k = k + 1
        sorted(collect)
        dst[i, j] = collect[5]

cv2.imshow('dst', dst)
cv2.waitKey(0)
