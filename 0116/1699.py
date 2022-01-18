import sys

n = int(input())

d = [0] * (n+1)

d[1] = 1

for i in range(2, n+1):
  d[i] = i
  j = 1
  while j*j <= i:
    if d[i] > d[i-j*j] + 1:
      d[i] = d[i-j*j] + 1
    j += 1

print(d[n])