n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]

d[0][0] = a[0][0]

for i in range(1, n):
  d[i][0] = d[i-1][0] + a[i][0]

# d[1][1] = a[0][0] + a[1][1]

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      continue
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]0

print(max(d[n-1]))
      