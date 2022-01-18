#1, 2, 3 더하기 3
import sys
input = sys.stdin.readline
mod = 1000000009

d = [0] * (1000001)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 1000001):
  d[i] = d[i-1] + d[i-2] + d[i-3]
  d[i] %= mod


t = int(input())
for _ in range(t):
  n = int(input())
  print(d[n])
