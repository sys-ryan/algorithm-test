from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

w, h = map(int, input().split())
a = [list(map(str, input())) for _ in range(h)]

sx=sy=es=ey=-1
for i in range(h):
  for j in range(w):
    if a[i][j] == 'C':
      if sx == -1:
        sx, sy = i, j
      else:
        ex, ey = i, j

dist = [[-1] * w for _ in range(h)]

q = deque()
q.append((sx, sy))
dist[sx][sy] = 0

while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    
    while 0 <= nx < h and 0 <= ny < w:
      if a[nx][ny] == '*':
        break
      if dist[nx][ny] == -1:
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))
      
      nx += dx[k]
      ny += dy[k]

print(dist[ex][ey] - 1)