#!/usr/bin/env python3
print("Hello World!")
import matplotlib.pyplot as plt
import numpy as np
print(np.__version__)
x=np.linspace(0,20,101)
print(x)
y=x*x
print(y)
plt.plot(x,y)
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.show()