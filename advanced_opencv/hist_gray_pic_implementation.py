# implementation of hist of gray pic

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../picture/opencv.jpg', 1)
info = img.shape
height = info[0]
width = info[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

count = np.zeros(256, np.float32)

for i in range(height):
    for j in range(width):
        index = int(gray[i, j])
        count[index] = count[index] + 1

for i in range(256):
    count[i] = count[i] / (height * width)

x = np.linspace(0, 255, 256)
y = count

plt.bar(x, y, 1, alpha=1, color='r')
plt.show()
cv2.waitKey(0)
