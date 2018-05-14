# implementaiton of equalizing hist of color pic

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

dst_b = np.zeros((height, width, 1), np.uint8)
dst_g = np.zeros((height, width, 1), np.uint8)
dst_r = np.zeros((height, width, 1), np.uint8)

count_b = np.zeros(256, np.float32)
count_g = np.zeros(256, np.float32)
count_r = np.zeros(256, np.float32)

for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        index_b = int(b)
        index_g = int(g)
        index_r = int(r)
        count_b[index_b] = count_b[index_b] + 1
        count_g[index_g] = count_g[index_g] + 1
        count_r[index_r] = count_r[index_r] + 1
for i in range(256):
    count_b[i] = count_b[i] / (height * width)
    count_g[i] = count_g[i] / (height * width)
    count_r[i] = count_r[i] / (height * width)

sum_b = np.float32(0.0)
sum_g = np.float32(0.0)
sum_r = np.float32(0.0)
for i in range(256):
    sum_b = sum_b + count_b[i]
    sum_g = sum_g + count_g[i]
    sum_r = sum_r + count_r[i]
    count_b[i] = sum_b
    count_g[i] = sum_g
    count_r[i] = sum_r

dst = np.zeros(info, np.uint8)

for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        dst[i, j] = (255 * count_b[b], 255 * count_g[g], 255 * count_r[r])
#         dst_b[i, j] = np.uint8(255 * count_b[b])
#         dst_g[i, j] = np.uint8(255 * count_g[g])
#         dst_r[i, j] = np.uint8(255 * count_r[r])
#
# dst = cv2.merge((dst_b, dst_g, dst_r))


cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
