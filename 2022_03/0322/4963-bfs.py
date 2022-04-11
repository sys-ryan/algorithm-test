# bfs

from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(x ,y, cnt):
  q = deque()
  q.append((x, y))
  check[x][y] = cnt

  while q:
    x, y = q.popleft()

    for k in range(8):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < h and 0 <= ny < w:
        if check[nx][ny] == 0 and a[nx][ny] != 0:
          q.append((nx, ny))
          check[nx][ny] = cnt

while True:
  w, h = map(int, input().split())
  
  if w == 0 and h == 0:
    break

  check = [[0] * w for _ in range(h)]
  a = [list(map(int, input().split())) for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if a[i][j] != 0 and check[i][j] == 0:
        cnt += 1
        bfs(i, j, cnt)

  print(cnt)

