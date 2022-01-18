#정수 삼각형 
import sys
input = sys.stdin.readline

n = int(input())

a = [[0] * n for _ in range(n)]
d = [[0] * n for _ in range(n)]

for i in range(n):
  s = list(map(int, input().split()))
  for j in range(i+1):
    a[i][j] = s[j]
  
for i in range(n):
  d[i][0] = d[i-1][0] + a[i][0]

for i in range(1, n):
  for j in range(1, i+1):
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]

print(max(d[n-1]))
