import numpy as np
import matplotlib.pyplot as plt

N_institute = 100
N = 10
counts = np.zeros((N_institute, 3))
for i in range(N_institute):
    # Set the approval rate of the candidate
    candidates = ['A', 'B', 'N/A']
    prob = np.array([0.5, 0.45, 0.05])

    # Randomly do the sampling
    sampling = np.random.choice(candidates, size=N, p=prob)
    print(np.unique(sampling, return_counts=True))
    unique, counts_ind = np.unique(sampling, return_counts=True)

    if counts_ind.shape == 2:
        counts[i, 0:3] = counts_ind
    else:
        counts[i, :] = counts_ind

approval_rate = counts/N

# Do the plot
plt.figure()
plt.hist(approval_rate[0], bins=100)
plt.show()

