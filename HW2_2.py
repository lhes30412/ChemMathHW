import numpy as np
import matplotlib.pyplot as plt

N_institute = 1000
N = 1000
counts = np.zeros((N_institute, 3))
for i in range(N_institute):
    # Set the approval rate of the candidate
    candidates = ['A', 'B', 'N/A']
    prob = np.array([0.5, 0.45, 0.05])

    # Randomly do the sampling
    sampling = np.random.choice(candidates, size=N, p=prob)
    # print(np.unique(sampling, return_counts=True))
    unique, counts_ind = np.unique(sampling, return_counts=True)

    if counts_ind.shape[0] == 2:
        counts[i, 0:2] = counts_ind.copy()
    else:
        counts[i, :] = counts_ind.copy()

approval_rate = counts/N
approval_rate = approval_rate[:, 0].T
mean = np.mean(approval_rate)
std = np.std(approval_rate)

print('Mean of the approval rate of A: %.3f\n' % mean)
print('Std of the approval rate of A: %.3f\n' % std)

# Do the plot
plt.figure()
hist_counts, hist_bins, patches = plt.hist(approval_rate, bins=15)
plt.title('Histogram of the approval rate of candidate A from 1000 institute')
plt.xlabel('Approval rate of candidate A')
plt.ylabel('Counts')
plt.show()
