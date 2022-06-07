from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]

q = deque()

q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
  x, y, z = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
        dist[nx][ny][z] = dist[x][y][z] + 1
        q.append((nx, ny, z))
      if z == 0 and a[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
        dist[nx][ny][z+1] = dist[x][y][z] + 1
        q.append((nx, ny, z+1))

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
  print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
  print(dist[n-1][n-2][0])
elif dist[n-1][m-1][1] != 0:
  print(dist[n-1][m-1][1])
else:
  print(-1)