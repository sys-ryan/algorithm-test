import sys

n = int(input())
a = [0] + [int(input()) for _ in range(n)]

d = [[0, 0] for _ in range(n+1)]

if n == 1:
  print(a[1])
  sys.exit(0)
elif n == 2:
  print(a[1] + a[2])
  sys.exit(0)


d[1][0] = 0
d[1][1] = a[1]
d[2][0] = a[1]
d[2][1] = a[1] + a[2]

for i in range(3, n+1):
  d[i][0] = max(d[i-1][0], d[i-1][1])
  d[i][1] = max(d[i-1][0], d[i-2][0] + a[i-1]) + a[i]

print(max(d[n]))
