# basic functions of numpy

import numpy as np

data1 = np.array([1, 2])
data2= np.array([[1, 2, 3],
                 [4, 5, 6]])
print(data1)
print(data2)
print(data1.shape, data2.shape) # dimensions 维度

data3 = np.zeros([3, 3])
data4 = np.ones([2, 4])
print(data3)
print(data4)

print(data3[2, 2])
data4[1, 1] = 5
print(data4)

print(data4 + 2)
print(data4 * np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))