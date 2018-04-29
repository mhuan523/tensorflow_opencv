# basic functions of matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([12, 14, 11, 22, 45, 78, 10, 33])

plt.plot(x, y, color = 'r', lw = 2, marker = '+')
plt.show()

plt.bar(x, y, 0.5, color = 'b', alpha = 1, )
plt.show()