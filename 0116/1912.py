import sys

n = int(input())
a = list(map(int, input().split()))

d = [-1] * n

for i in range(n):
  d[i] = a[i]

  if d[i] < d[i-1] + a[i]:
    d[i] = d[i-1] + a[i]


print(max(d))