import numpy as np

def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5

    return result

#l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1)))
#l2_dist(a.T, b.T)
#l2_dist(a, b)
l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20)))