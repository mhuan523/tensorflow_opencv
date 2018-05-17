# svm in opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt

boy = np.array([[160, 51], [165, 55], [176, 67], [178, 70], [186, 75]])
girl = np.array([[155, 45], [160, 47], [165, 54], [163, 50], [173, 60]])

data = np.vstack((boy, girl))
data = np.array(data, dtype=np.float32)
lable = np.array([[1], [1], [1], [1], [1], [0], [0], [0], [0], [0]])

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

result = svm.train(data, cv2.ml.ROW_SAMPLE, lable)

predict_data = np.vstack([[156, 46],[180, 71]])
predict_data = np.array(predict_data, dtype='float32')

predict_result = svm.predict(predict_data)

print(predict_result)
