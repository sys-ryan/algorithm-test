from collections import deque

r, c = map(int, input().split())
a = [list(map(str, input())) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

water = [[-1] * c for _ in range(r)]
dist = [[-1] * c for _ in range(r)]

q = deque()

for i in range(r):
  for j in range(c):
    if a[i][j] == '*':
      q.append((i, j))
      water[i][j] = 0
    elif a[i][j] == 'S':
      sx, sy = i, j
    elif a[i][j] == 'D':
      ex, ey = i, j

# 시간에 따른 물의 경로
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < r and 0 <= ny < c:
      if water[nx][ny] != -1:
        continue
      if a[nx][ny] in 'XD':
        continue
      
      water[nx][ny] = water[x][y] + 1
      q.append((nx, ny))

q.append((sx, sy))
dist[sx][sy] = 0
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < r and 0 <= ny < c:
      if dist[nx][ny] != -1:
        continue
      if a[nx][ny] == 'X':
        continue
      if water[nx][ny] != -1 and dist[x][y] + 1 >= water[nx][ny]:
        continue

      dist[nx][ny] = dist[x][y] + 1
      q.append((nx, ny))


if dist[ex][ey] == -1:
  print("KAKTUS")
else:
  print(dist[ex][ey])