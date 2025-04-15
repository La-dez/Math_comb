from generators.combinatorics.my_generators import *
from generators.combinatorics.itertools_generators import *

test_array = ['A', 'B', 'C', 'D']
# generate_permutations(['A', 'B', 'C', 'D'])#перестановки
# generate_arrangements(['A', 'B', 'C', 'D'],3) #размещения
# generate_combinations(['A', 'B', 'C', 'D'], 2) #сочетания
generate_product(['A', 'B', 'C', 'D'], 2) #сочетания с повторениями
# generate_combinations_with_replacement(['A', 'B', 'C', 'D'], 2) #сочетания с повторениями

# itertools_permutations(test_array)
# itertools_arrangements(test_array, 2)
itertools_combinations(test_array, 2)
# itertools_product(test_array, repeat=2) 
# itertools_combinations_with_replacement(test_array, r=2)


