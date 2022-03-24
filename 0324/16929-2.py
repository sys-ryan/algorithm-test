import sys
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]


def dfs(x, y, color, count):
  if dist[x][y] != -1:
    return (count - dist[x][y]) >= 4

  dist[x][y] = count
  
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == color: 
        if dfs(nx, ny, color, count+1):
          return True
  
  return False


for i in range(n):
  for j in range(m):
    if dist[i][j] == -1:
      if dfs(i, j, a[i][j], 0):
        print("YES")
        sys.exit()

print("NO")