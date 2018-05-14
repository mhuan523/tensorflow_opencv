# equalize hist of color pic using opencv

import cv2
import numpy as np

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
cv2.imshow('src', img)

(b, g, r) = cv2.split(img)

bHist = cv2.equalizeHist(b)
gHist = cv2.equalizeHist(g)
rHist = cv2.equalizeHist(r)

dst = cv2.merge((bHist, gHist, rHist))

cv2.imshow('dst', dst)
cv2.waitKey(0)

