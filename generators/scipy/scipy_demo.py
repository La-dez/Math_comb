# pmf — probability mass function (для дискретных)
# pdf — probability density function (для непрерывных)
# cdf — cumulative distribution function
# ppf — percent point function (обратная CDF)
# rvs — генерация случайных значений

from scipy.stats import binom, hypergeom, norm
import numpy as np

# === БИНОМИАЛЬНОЕ РАСПРЕДЕЛЕНИЕ ===
binom_dist = binom(n=5, p=1/6)
print("\n📘 BINOMIAL (n=5, p=1/6)")
print("P(X = 3):", binom_dist.pmf(3))
print("P(X ≤ 3):", binom_dist.cdf(3))
print("P(X ≥ 3):", 1 - binom_dist.cdf(2))
print("Quantile 90%:", binom_dist.ppf(0.9))
print("Random sample:", binom_dist.rvs(size=5))

# === ГИПЕРГЕОМЕТРИЧЕСКОЕ РАСПРЕДЕЛЕНИЕ ===
hypergeom_dist = hypergeom(M=20, n=6, N=5)
print("\n📘 HYPERGEOMETRIC (N=20, good=6, sample=5)")
print("P(X = 2):", hypergeom_dist.pmf(2))
print("P(X ≤ 2):", hypergeom_dist.cdf(2))
print("P(X ≥ 2):", 1 - hypergeom_dist.cdf(1))
print("Quantile 80%:", hypergeom_dist.ppf(0.8))
print("Random sample:", hypergeom_dist.rvs(size=5))

# === НОРМАЛЬНОЕ РАСПРЕДЕЛЕНИЕ ===
normal_dist = norm(loc=0, scale=1)
print("\n📘 NORMAL (μ=0, σ=1)")
print("P(X < 1.5):", normal_dist.cdf(1.5))
print("P(1 < X < 2):", normal_dist.cdf(2) - normal_dist.cdf(1))
print("Quantile 97.5%:", normal_dist.ppf(0.975))  # ≈ 1.96
print("P(|X| ≤ 2):", normal_dist.cdf(2) - normal_dist.cdf(-2))
print("Random sample:", normal_dist.rvs(size=5))