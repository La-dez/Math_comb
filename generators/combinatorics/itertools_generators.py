from itertools import combinations_with_replacement, permutations, combinations, product
def result_printer(fun):
    def printEvery(*args,**kwargs):
        result = fun(*args,**kwargs)
        [print(el) for el in result]

    # Decorator returns a function
    return printEvery


# Все перестановки:
@result_printer
def itertools_permutations(arr): return permutations(arr) # по умолчанию длина = len(seq)

# Размещения (перестановки длины < n):
@result_printer
def itertools_arrangements(arr, k): return permutations(arr, k) # длина = k

# Сочетания:
@result_printer
def itertools_combinations(arr, k): return combinations(arr, k) # длина = k

# Размещения с повторениями (product):
@result_printer
def itertools_product(arr, repeat): return product(arr, repeat=repeat) # включает [1,1], [1,2], ...

# Сочетания с повторениями (product):
@result_printer
def itertools_combinations_with_replacement(arr, r): return combinations_with_replacement(arr, r=r) # включает [1,1], [1,2], ...

