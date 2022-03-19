# 2667 dfs

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
d = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
  d[x][y] = c

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < n:
      if a[nx][ny] != 0 and d[nx][ny] == 0:
        dfs(nx, ny, c)

cnt = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and d[i][j] == 0:
      cnt += 1
      dfs(i, j, cnt)
print(cnt)

ans = [0] * (cnt+1)
for i in range(n):
  for j in range(n):
    for k in range(1, cnt+1):
      if d[i][j] == k:
        ans[k] += 1

ans.sort()

for i in range(1, cnt+1):
  print(ans[i])
