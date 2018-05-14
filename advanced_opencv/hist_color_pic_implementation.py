# implementation of hist of color pic

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

countB = np.zeros(256, np.float32)
countG = np.zeros(256, np.float32)
countR = np.zeros(256, np.float32)

(b, g, r) = cv2.split(img)

for i in range(height):
    for j in range(width):
        indexB = b[i, j]
        indexG = g[i, j]
        indexR = r[i, j]
        countB[indexB] = countB[indexB] + 1
        countG[indexG] = countG[indexG] + 1
        countR[indexR] = countR[indexR] + 1

for i in range(256):
    countB[i] = countB[i] / (height * width)
    countG[i] = countG[i] / (height * width)
    countR[i] = countR[i] / (height * width)

x = np.linspace(0, 255, 256)
yB = countB
yG = countG
yR = countR

plt.bar(x, yB, 1, alpha=0.9, color='b')
plt.figure()
plt.bar(x, yG, 1, alpha=0.9, color='g')
plt.figure()
plt.bar(x, yR, 1, alpha=0.9, color='r')
plt.figure()

plt.show()
