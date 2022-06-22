n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

d = [[0]*n for _ in range(n)]

d[0][0] = a[0][0]
for i in range(1, n):
  for j in range(0, i+1):
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]

print(max(d[n-1]))