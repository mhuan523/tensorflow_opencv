# resize pic using warpAffine

import cv2
import numpy as np

img = cv2.imread('../picture/mountain.jpg', 1)
info = img.shape
height = info[0]
width = info[1]
mode = info[2]

scaleMat = np.float32([[0.5, 0, 0], [0, 0.5, 0]])

dst = cv2.warpAffine(img, scaleMat, (int(width / 2), int(height / 2)))

#v2.imwrite('../picture/mountain_resize_warpAffine.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey(0)