# resize pic using opencv
import cv2

img = cv2.imread('../picture/opencv.jpg', 1)
shape = img.shape
height = int(shape[0] * 0.5)
width = int(shape[1] * 0.5)
mode = shape[2]
dst = cv2.resize(img, (height, width))
cv2.imshow("dst", dst)
cv2.waitKey(0)
