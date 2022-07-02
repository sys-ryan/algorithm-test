dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

dist = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]

def dfs(x, y, cnt, color):
  if check[x][y]:
    return cnt - dist[x][y] >= 4

  check[x][y] = True
  dist[x][y] = cnt

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == color:
        if dfs(nx, ny, cnt+1, color):
          return True
  return False

for i in range(n):
  for j in range(m):
    if check[i][j]:
      continue
    dist = [[0]*m for _ in range(n)]
    ok = dfs(i, j, 1, a[i][j])
    if ok:
      print("Yes")
      exit()
print("No")