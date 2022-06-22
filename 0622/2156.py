import sys
n = int(input())
a = []
for _ in range(n):
  a.append(int(input()))

if n == 1:
  print(a[0])
  sys.exit()
  
d = [[0]*2 for _ in range(n)]

d[0][0] = 0
d[0][1] = a[0]
d[1][0] = max(d[0][0], d[0][1])
d[1][1] = a[0] + a[1]

for i in range(2, n):
  d[i][0] = max(d[i-1][1], d[i-1][0])
  d[i][1] = max(a[i-1] + d[i-2][0], d[i-1][0]) + a[i]

print(max(d[n-1]))