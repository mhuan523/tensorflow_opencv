# hist pic using opencv

import cv2
import numpy as np


def hist(image, type=None):
    color = (255, 255, 255)
    winName = 'gray'
    if type == 30:
        color = (255, 0, 0)
        winName = 'B Hist'
    elif type == 31:
        color = (0, 255, 0)
        winName = 'G Hist'
    elif type == 32:
        color = (0, 0, 255)
        winName = 'R Hist'

    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    _, maxV, _, _ = cv2.minMaxLoc(hist)
    histImg = np.zeros((256, 256, 3), np.uint8)
    for i in range(256):
        intenseNomal = int(hist[i] * 256 / maxV)
        cv2.line(histImg, (i, 256), (i, 256 - intenseNomal), color)
    cv2.imshow(winName, histImg)
    return histImg

img = cv2.imread('../picture/opencv.jpg', 1)
channels = cv2.split(img)

for i in range(3):
    hist(channels[i], i + 30)

cv2.waitKey(0)