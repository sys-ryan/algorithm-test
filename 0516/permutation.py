from itertools import permutations, combinations

items = ['1', '2', '3', '4']

print('Permutation: ', list(map(''.join, permutations(items, 2))))
print('Combination: ', list(map(''.join, combinations(items, 2))))