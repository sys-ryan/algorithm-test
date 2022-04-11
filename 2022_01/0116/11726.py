import sys

d = [-1] * 1001
mod = 10007

n = int(input())

if n <= 3:
  print(n)
  sys.exit(0)

d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4, n+1):
  d[i] = d[i-1] + d[i-2]
  d[i] %= mod

print(d[n])