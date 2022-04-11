from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(x, y, cnt):
  q = deque()
  q.append((x, y))
  d[x][y] = cnt

  while q:
    x, y = q.popleft()
    for k in range(8):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < h and 0 <= ny < w:
        if a[nx][ny] == 1 and d[nx][ny] == 0:
          d[nx][ny] = cnt
          q.append((nx, ny))

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  a = [list(map(int, input().split())) for _ in range(h)]
  d = [[0] * w for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if a[i][j] != 0 and d[i][j] == 0:
        cnt += 1
        bfs(i, j, cnt)

  print(cnt)