# filter pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

guassian_img = cv2.GaussianBlur(img, (5, 5), 0)

bilateral_img = cv2.bilateralFilter(img, 15, 35, 35)

cv2.imshow('dst_guassian', guassian_img)
cv2.imshow('dst_bilateral', bilateral_img)
cv2.waitKey(0)
