#이친수

import sys
input = sys.stdin.readline

d = [[0]*2 for _ in range(91)]

n = int(input())

d[1][0] = 0
d[1][1] = 1

for i in range(2, n+1):
  d[i][0] = d[i-1][0] + d[i-1][1]
  d[i][1] = d[i-1][0]

print(sum(d[n]))

