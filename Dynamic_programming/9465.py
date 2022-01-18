#스티커 
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
  n = int(input())

  d = [[0] * 3 for _ in range(n+1)]
  a = [[0] * 2 for _ in range(n+1)]

  a1 = list(map(int, input().split()))
  a2 = list(map(int, input().split()))

  for i in range(1, n+1):
    a[i][0] = a1[i-1]
    a[i][1] = a2[i-1]
  
  d[1][0] = 0
  d[1][1] = a[1][0]
  d[1][2] = a[1][1]

  for i in range(2, n+1):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = max(d[i-1][0], d[i-1][2]) + a[i][0]
    d[i][2] = max(d[i-1][0], d[i-1][1]) + a[i][1]

  print(max(d[n][0], d[n][1], d[n][2]))



