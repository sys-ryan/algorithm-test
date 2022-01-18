#연속합
import sys
input = sys.stdin.readline

n = int(input())

a = '-1001 '
a += input()
a = list(map(int, a.split()))

d = [-1001] * (n+1)

for i in range(1, n+1):
  d[i] = a[i]
  if i > 1 and d[i] < d[i-1] + a[i]:
    d[i] = d[i-1] + a[i]


print(max(d))