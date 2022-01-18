import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)

if n == 1:
  print(1)
  sys.exit(0)

if n == 2:
  print(1)
  sys.exit(0)

if n == 3:
  print(2)
  sys.exit(0)

d[1] = 1
d[2] = 1
d[3] = 2

for i in range(4, n+1):
  d[i] = d[n-1] + d[n-2]

print(d[n])
