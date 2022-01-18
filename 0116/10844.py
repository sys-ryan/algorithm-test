import sys

n = int(input())
mod = 1000000000

d = [[0] * (10) for _ in range(101)]


for i in range(1, 10):
  d[1][i] = 1

if n == 1:
  print(sum(d[1]))
  sys.exit(0)

for i in range(2, n+1):
  for j in range(0, 10):
    if j-1 >= 0: 
      d[i][j] += d[i-1][j-1]
    if j+1 <= 9:
      d[i][j] += d[i-1][j+1]
  
    d[i][j] %= mod

print(sum(d[n]) % mod)


