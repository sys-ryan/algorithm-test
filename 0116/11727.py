import sys

n = int(input())
mod = 10007
d = [0] * (1001)

d[1] = 1
d[2] = 3
d[3] = 5

if n <= 3:
  print(d[n])
  sys.exit(0)

for i in range(4, n+1):
  d[i] = d[i-1] + 2*d[i-2]
  d[i] %= mod

print(d[n])
