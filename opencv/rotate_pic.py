# rotate pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)


matRotate = cv2.getRotationMatrix2D((height / 2, width / 2), 45, 0.5)
dst = cv2.warpAffine(img, matRotate, (height, width))

cv2.imshow('dst', dst)
cv2.waitKey(0)