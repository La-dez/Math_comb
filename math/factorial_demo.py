from math import comb, factorial

def factorial_own(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(comb(5, 2))  # → 10
print(comb(6, 3))  # → 20
print(factorial(6)) # → 720
print(factorial_own(6)) # → 720
