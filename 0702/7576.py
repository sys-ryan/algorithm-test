from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


q = deque()

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      q.append((i, j))
      dist[i][j] = 0

while q:
  x, y = q.popleft()

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]

    if 0 <= nx < n and 0 <= ny < m:
      if dist[nx][ny] == -1 and box[nx][ny] == 0:
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))
  
for i in range(n):
  for j in range(m):
    if box[i][j] == 0 and dist[i][j] == -1:
      print(-1)
      exit()

max_val = 0
for i in range(n):
  for j in range(m):
    max_val = max(max_val, dist[i][j])

print(max_val)  