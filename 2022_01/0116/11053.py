import sys

n = int(input())
a = list(map(int, input().split()))

d = [0] * (n)

for i in range(n):
  d[i] = 1

  if i == 0:
    continue

  for j in range(i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1

print(max(d))
