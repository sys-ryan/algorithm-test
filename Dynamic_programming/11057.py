#오르막 수
import sys
input = sys.stdin.readline
mod = 10007
d = [ [0] * 10 for _ in range(1001)]

for i in range(0, 10):
  d[1][i] = 1

n = int(input())

for i in range(2, n+1):
  for j in range(0, 10):
    for k in range(0, j+1):
      d[i][j] += d[i-1][k]
      d[i][j] %= mod

print(sum(d[n]) % mod)

#오르막 수
import sys
input = sys.stdin.readline
mod = 10007
d = [ [0] * 10 for _ in range(1001)]

for i in range(0, 10):
  d[1][i] = 1

n = int(input())

for i in range(2, n+1):
  for j in range(0, 10):
    for k in range(0, j+1):
      d[i][j] += d[i-1][k]
      d[i][j] %= mod

print(sum(d[n]) % mod)

