import sys

n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
d = [[0] * (n) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, c):
  d[x][y] = c

  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < n and 0 <= ny < n:
      if a[nx][ny] == 1 and d[nx][ny] == 0:
        dfs(nx, ny, c)
  
cnt = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and d[i][j] == 0:
      cnt += 1
      dfs(i, j, cnt)

print(cnt)

ans = []
for k in range(1, cnt+1):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if d[i][j] == k:
        cnt += 1

  ans.append(cnt)


ans.sort()

for el in ans:
  print(el)
