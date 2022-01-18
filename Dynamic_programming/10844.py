#쉬운 계단수 
import sys

input = sys.stdin.readline

n = int(input())
mod = 1000000000

d = [[0]*10 for _ in range(100+1)]

for i in range(1, 10):
  d[1][i] = 1

for i in range(2, n+1):
  for j in range(0, 10):
    d[i][j] = 0
    if j-1 >= 0:
      d[i][j] += d[i-1][j-1]
    if j+1 <= 9:
      d[i][j] += d[i-1][j+1]

    d[i][j] %= mod

print(sum(d[n]) % mod)

