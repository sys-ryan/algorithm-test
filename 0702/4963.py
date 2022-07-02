from collections import deque 

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(sx, sy):
  check[sx][sy] = True
  q = deque()
  q.append((sx, sy))

  while q:
    x, y = q.popleft()

    for k in range(8):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < h and 0 <= ny < w:
        if not check[nx][ny] and word[nx][ny] == 1:
          check[nx][ny] = True
          q.append((nx, ny))
            

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  word = [list(map(int, input().split())) for _ in range(h)]
  check = [[False]*w for _ in range(h)]

  islands_count = 0
  for i in range(h):
    for j in range(w):
      if word[i][j] == 1 and not check[i][j]:
        islands_count += 1
        bfs(i, j)

  print(islands_count)