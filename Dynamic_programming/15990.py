# 1, 2, 3 더하기 5 (연속 불가능)
import sys
input = sys.stdin.readline

t = int(input())

limit = 100001
mod = 1000000009
d = [[0] * 4 for _ in range(limit+1)]

for i in range(1, limit+1):
  if i-1 >= 0:
    d[i][1] = d[i-1][2] + d[i-1][3]
    if i == 1:
      d[i][1] = 1
  
  if i-2 >= 0:
    d[i][2] = d[i-2][1] + d[i-2][3]
    if i == 2:
      d[i][2] = 1
  
  if i-3 >= 0:
    d[i][3] = d[i-3][1] + d[i-3][2]
    if i == 3:
      d[i][3] = 1

  d[i][1] %= mod
  d[i][2] %= mod
  d[i][3] %= mod


for _ in range(t):
  n = int(input())
  print(sum(d[n]) % mod)

  
