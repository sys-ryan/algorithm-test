#다음 순열
import sys
from itertools import permutations
n = int(input())
a = list(map(int, input().split()))

b = list(i for i in range(1, n+1))

perm_list = list(map(list, permutations(b)))
# print(perm_list)

if perm_list[-1] == a:
  print(-1)
  sys.exit(0)

for idx, el in enumerate(perm_list):
  if el == a:
    print(' '.join(map(str, perm_list[idx+1])))