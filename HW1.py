import numpy as np
import time
from scipy.spatial import distance_matrix

# For 2D circle
N = 500000
count = 0
# Generate random points and origin point
t = time.time()
random_point = np.random.random([N, 2])
origin = np.array([[0, 0]])

dist = distance_matrix(origin, random_point)

for i in range(N):
    if dist[0][i] < 1:
        count += 1

prob = count/N
pi = prob*4
print(pi)
print('Total time taken for calculating pi by for loops in 2D model: %.3f sec' % (time.time() - t))

# for 3D model
t = time.time()
count = 0
random_point = np.random.random([N, 3])
origin = np.array([[0, 0, 0]])

dist = distance_matrix(origin, random_point)

for i in range(N):
    if dist[0][i] < 1:
        count += 1
prob = count/N
pi = prob*6
print(pi)
print('Total time taken for calculating pi by for loops in 3D model: %.3f sec' % (time.time() - t))

# Test by using np.where
# For 2D circle
count = 0
# Generate random points and origin point
t = time.time()
random_point = np.random.random([N, 2])
origin = np.array([[0, 0]])

dist = distance_matrix(origin, random_point)

within_points = np.where(dist[0] < 1)
shape = np.shape(within_points)
count = shape[1]

prob = count/N
pi = prob * 4
print(pi)
print('Total time taken for calculating pi by numpy.where in 2D model: %.3f sec' % (time.time() - t))
# for 3D
t = time.time()
count = 0
random_point = np.random.random([N, 3])
origin = np.array([[0, 0, 0]])

dist = distance_matrix(origin, random_point)

within_points = np.where(dist[0] < 1)
shape = np.shape(within_points)
count = shape[1]

prob = count/N
pi = prob*6
print(pi)
print('Total time taken for calculating pi by numpy.where in 3D model: %.3f sec' % (time.time() - t))
print('Program works successfully!! Go buy some beer!!')
