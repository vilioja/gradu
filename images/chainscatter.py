import matplotlib.pyplot as plt
import numpy as np
import random

x = np.zeros(11)
y = np.zeros(11)
#random.seed(9856)
for i in range(1,11):
    x[i] = random.uniform(-10,10)
    y[i] = random.uniform(-10,10)

plt.scatter(x,y)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.axes().set_aspect('equal')
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.show()
