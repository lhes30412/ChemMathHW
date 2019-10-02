import numpy as np
from scipy.spatial import distance_matrix

# For 2D circle
N = 100000000
count = 0
# Generate random points and origin point
random_point = np.random.random([N, 2])
origin = np.array([[0, 0]])

dist = distance_matrix(origin, random_point)

for i in range(N):
    if dist[0][i] < 1:
        count += 1

prob = count/N
pi = prob*4
print(pi)
print('Program works successfully, go buy some beers!!')

# for 3D
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
print('Program works successfully again!! More beers!!')
