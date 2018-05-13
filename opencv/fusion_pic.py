# fusion pic with opencv

import cv2
import numpy as np

img1 = cv2.imread('../picture/opencv.jpg', 1)
img2 = cv2.imread('../picture/glass.jpg', 1)
info = img1.shape
height = info[0]
width = info[1]
mode = info[2]

roiHeight = int(height)
roiWidth = int(width)

roiImg1 = img1[:roiHeight, : roiWidth]
roiImg2 = img2[:roiHeight, : roiWidth]

dst = np.zeros((roiHeight, roiWidth, 3), np.uint8)

dst = cv2.addWeighted(roiImg1, 0.5, roiImg2, 0.5, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)

