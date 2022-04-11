import sys

t = int(input())

for _ in range(t):
  n = int(input())

  a = [list(map(int, input().split())) for _ in range(2)]

  d = [[0, 0, 0] for _ in range(n+1)]


  d[1][0] = 0
  d[1][1] = a[0][0]
  d[1][2] = a[1][0]
  
  for i in range(2, n+1):
    d[i][0] = max(d[i-1][1], d[i-1][2])
    d[i][1] = max(d[i-1][0], d[i-1][2]) + a[0][i-1]
    d[i][2] = max(d[i-1][0], d[i-1][1]) + a[1][i-1]


  print(max(d[n]))
  
