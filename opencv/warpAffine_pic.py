# warpAffine pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]

dst = np.zeros(info, np.uint8)

matSrc = np.array([[0, 0], [0, width - 1], [height - 1, 0]], np.float32)
matDst = np.float32([[10, 10], [30, width - 30], [height - 20, 20]])
matAffine = cv2.getAffineTransform(matSrc, matDst)

dst = cv2.warpAffine(img, matAffine, (width, height))

cv2.imshow('dst', dst)
cv2.waitKey(0)
