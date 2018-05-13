# detect edge of pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]
cv2.imshow('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussainImg = cv2.GaussianBlur(gray, (3, 3), 0)

dst = cv2.Canny(gaussainImg, 50, 50)

cv2.imshow('dst', dst)
cv2.waitKey(0)
