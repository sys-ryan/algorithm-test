from collections import deque 
import sys

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]

q = deque()

for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      q.append((i, j))
      d[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
  x, y = q.popleft()

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]

    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 0 and d[nx][ny] == -1:
        q.append((nx, ny))
        d[nx][ny] = d[x][y] + 1

ok = True
day = 0
for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and d[i][j] == -1:
      ok = False
      print(-1)
      sys.exit()
    if d[i][j] > day:
      day = d[i][j]

print(day)