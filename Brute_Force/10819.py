import sys
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
a.sort()

perm = list(map(list, permutations(a)))

def calc(a):
  ans = 0
  for i in range(1, n):
    ans += abs(a[i] - a[i-1])

  return ans

ans = 0
for p in perm:
  temp = calc(p)
  # print(temp)
  ans = max(ans, temp)

print(ans)