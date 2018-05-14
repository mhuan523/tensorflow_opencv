# implementaiton of equalizing hist of gray pic

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)

count = np.zeros(256, np.float32)

for i in range(height):
    for j in range(width):
        index = gray[i, j]
        count[index] = count[index] + 1
for i in range(256):
    count[i] = count[i] / (height * width)

sum = np.float32(0.0)
for i in range(256):
    sum = sum + count[i]
    count[i] = sum

for i in range(height):
    for j in range(width):
        dst[i, j] = np.uint8(255 * count[gray[i, j]])

cv2.imshow('src', gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)
