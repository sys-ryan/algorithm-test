import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      q.append((i, j))
      d[i][j] = 0


while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 0 and d[nx][ny] == -1:
        d[nx][ny] = d[x][y] + 1
        q.append((nx, ny))

ans = -1
for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and d[i][j] == -1:
      print(-1)
      sys.exit(0)
    ans = max(ans, d[i][j])

print(ans) 
      

    


  