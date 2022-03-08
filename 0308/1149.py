import sys
input = sys.stdin.readline

n = int(input())
a = [[0, 0, 0] for _ in range(n+1)]
d = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
  a[i][0], a[i][1], a[i][2] = map(int, input().split())

d[1][0] = a[1][0]
d[1][1] = a[1][1]
d[1][2] = a[1][2]

for i in range(2, n+1):
  d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
  d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
  d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]

print(min(d[n]))
