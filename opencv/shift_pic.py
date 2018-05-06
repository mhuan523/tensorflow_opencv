# shift pic using opencv

import numpy as np
import cv2

img = cv2.imread('../picture/mountain.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]

shiftMat = np.array([[1, 0, 100], [0, 1, 200]], dtype=np.float32)  # shift mat
dst = cv2.warpAffine(img, shiftMat, (width, height))

cv2.imshow('dst', dst)
cv2.waitKey(0)
