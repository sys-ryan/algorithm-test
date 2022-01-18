# 2xN 타일

import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)

if n <= 2:
  print(n)
  sys.exit(0)

d[1] = 1
d[2] = 2

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]
  d[i] %= 10007
  
print(d[n])