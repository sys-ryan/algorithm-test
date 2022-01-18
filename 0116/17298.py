import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

s = [0]
ans = [0] * n

for i in range(1, n):
  while s and a[i] > a[s[-1]]:
    ans[s[-1]] = a[i]
    s.pop()
  s.append(i)


for i in range(n):
  if ans[i] == 0:
    ans[i] = -1

for el in ans:
  print(el, end=' ')
print()
