# oil painting of pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = np.zeros((height, width, 3), np.uint8)

for i in range(-4, height - 4):
    for j in range(-4, width - 4):
        array1 = np.zeros(8, np.uint8)
        for m in range(-4, 4):
            for n in range(-4, 4):
                p1 = int(gray[i + m, j + n] / 32)
                array1[p1] = array1[p1] + 1
        currentMax = 0
        l = 0
        for k in range(8):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        for m in range(-4, 4):
            for n in range(-4, 4):
                if gray[i + m, j + n] >= l * 32 and gray[i + m, j + n] <= (l + 1) * 32:
                    (b, g, r) = img[i + m, j + n]
        dst[i, j] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)
