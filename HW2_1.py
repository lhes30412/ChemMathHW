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
plt.plot(x, y, '.', label='Data')
plt.plot(x, A@c, '-', label='Fitting curve')
plt.legend(loc='best')
plt.show()
'''
# Using scipy.optimize
# Fitting function

fun = lambda _a, _b, _c, _d, _x: _a * pow(_x, _b) * np.cos(_c * _x - _d)
fun_err = lambda _a, _b, _c, _d, _x: abs(fun(_a, _b, _c, _d, _x) - y) ** 2

result, success = minimize(fun_err, (0, 0, 0, 0))

if success:
    print(result)
'''
