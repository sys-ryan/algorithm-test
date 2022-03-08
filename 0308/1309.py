import sys
input = sys.stdin.readline

mod = 9901
n = int(input())

d = [[0, 0, 0] for _ in range(n)]

d[0][0] = d[0][1] = d[0][2] = 1

for i in range(1, n):
  d[i][0] = d[i-1][0] + d[i-1][1] + d[i-1][2]
  d[i][1] = d[i-1][0] + d[i-1][2]
  d[i][2] = d[i-1][0] + d[i-1][1]

  d[i][0] %= mod
  d[i][1] %= mod
  d[i][2] %= mod

print(sum(d[n-1]) % mod)
