# tensorflow module
import tensorflow as tf

constant = tf.constant('hello world!')
session = tf.Session()
print(session.run(constant))

# opencv module
import cv2

img = cv2.imread('../picture/mountain.jpg', 1)
cv2.imshow('flower', img)
cv2.waitKey(0)