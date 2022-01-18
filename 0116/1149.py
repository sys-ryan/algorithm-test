import sys

n = int(input())
a = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

d = [[0] * 3 for _ in range(n+1)]

d[1][0] = a[1][0]
d[1][1] = a[1][1]
d[1][2] = a[1][2]

for i in range(2, n+1):
  d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
  d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
  d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]

print(min(d[n]))

