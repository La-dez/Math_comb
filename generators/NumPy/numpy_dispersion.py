import numpy as np


x = np.array([2, 4, 4, 4, 5, 5, 7, 9])

mean = np.mean(x)
squared_diffs = (x - mean) ** 2
variance_manual = np.sum(squared_diffs) / len(x)
variance_numpy = np.var(x)
sample_variance_numpy = np.var(x, ddof=1)  # Sample variance (N-1 in the denominator)
print("Mean:", mean)
print("Manual variance:", variance_manual)
print("NumPy variance:", variance_numpy)
print("Sample NumPy variance variance:", sample_variance_numpy)