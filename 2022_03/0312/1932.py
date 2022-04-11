import sys
input = sys.stdin.readline

n = int(input())

d = [[0 for _ in range(n+1)] for _ in range(n+1)]
t = []

for i in range(n):
  t.append(list(map(int, input().split())))

d[0][0] = t[0][0]
for i in range(1, n):
  d[i][0] = d[i-1][0] + t[i][0]

for i in range(1, n):
  for j in range(1, i+1):
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + t[i][j]


print(max(d[n-1]))