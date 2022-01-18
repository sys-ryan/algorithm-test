import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y, cnt):
  d[x][y] = cnt
  
  for k in range(8):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < h and 0 <= ny  < w:
      if a[nx][ny] == 1 and d[nx][ny] == 0:  
        dfs(nx, ny, cnt)


while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  a = [list(map(int, input().split())) for _ in range(h)]
  d = [[0] * w for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if a[i][j] == 1 and d[i][j] == 0:
        cnt += 1
        dfs(i, j, cnt)
    
  print(cnt)
        
  


