import sys
sys.setrecursionlimit(10**6)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(x, y, cnt):
  check[x][y] = cnt

  for k in range(8):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < h and 0 <= ny < w:
      if check[nx][ny] == 0 and a[nx][ny] != 0:
        dfs(nx, ny, cnt)
      

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  a = [list(map(int, input().split())) for _ in range(h)]
  check = [[0] * w for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if check[i][j] == 0 and a[i][j] != 0:
        cnt += 1
        dfs(i, j, cnt)

  print(cnt)




