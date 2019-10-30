import numpy as np
import matplotlib.pyplot as plt
import scipy.special
from scipy.optimize import minimize

# First, construct the target function
x = np.linspace(0, 30, 1001)
y = x*scipy.special.jv(1, x)

# Second, build the cos polynomial
order = 101
A_lst = []
for i in range(order):
    A_lst.append(np.cos(i * x))

A = np.array(A_lst).T

# Least Square method
c = np.linalg.solve(A.T@A, A.T@y)

# Plot
plt.plot(x, y, '.')
plt.plot(x, A@c, '-')
plt.show()

# Using scipy.optimize
# Fitting function
'''
fun = lambda
res = minimize(y, )
'''
