import numpy as np

# Биномиальное распределение
np.random.binomial(n=10, p=0.5, size=1000)

# Гипергеометрическое
np.random.hypergeometric(ngood=6, nbad=4, nsample=3, size=10000)

# Нормальное
np.random.normal(loc=0, scale=1, size=1000)

# print(np.random.hypergeometric(ngood=6, nbad=4, nsample=3, size=10))

print(np.random.normal(loc=0, scale=1, size=10))