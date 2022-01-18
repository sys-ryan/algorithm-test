#모든 순열
from itertools import permutations

n = int(input())
l = [i for i in range(1, n+1)]

for li in list(permutations(l)):
  for el in li:
    print(el, end=' ')
  print()