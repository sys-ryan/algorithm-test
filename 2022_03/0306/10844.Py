import sys
input = sys.stdin.readline

d = [[0 for _ in range (10)] for _ in range(101)]
mod = 1000000000
for i in range(1, 10):
  d[1][i] = 1

n = int(input())

for i in range(2, n+1):
  for j in range(0, 10):
    if j > 0:
      d[i][j] += d[i-1][j-1]
    if j < 9:
      d[i][j] += d[i-1][j+1]
    
    d[i][j] %= mod

print(sum(d[n]) % mod)