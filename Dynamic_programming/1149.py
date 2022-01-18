#RGB 거리 
import sys
input = sys.stdin.readline

n = int(input())
d = [[0] * 3 for _ in range(n+1)]
a = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
  a[i][0], a[i][1], a[i][2] = map(int, input().split())
  

for i in range(3):
  d[1][i] = a[1][i]

for i in range(1, n+1):
  d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
  d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
  d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]

print(min(d[n][0], d[n][1], d[n][2]))