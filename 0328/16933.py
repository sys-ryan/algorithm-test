from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, l = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
dist = [[[[0]*2 for _ in range(11)] for _ in range(m)] for _ in range(n)]

def bfs(x, y, z, night):
  q = deque()
  q.append((x, y, z, night))
  dist[x][y][z][night] = 1

  while q:
    x, y, z, night = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 0 and dist[nx][ny][z][1-night] == 0:
          dist[nx][ny][z][1-night] = dist[x][y][z][night] + 1
          q.append((nx, ny, z, 1-night))
        if night == 0 and z+1 <= l and a[nx][ny] == 1 and dist[nx][ny][z+1][1-night] == 0:
          dist[nx][ny][z+1][1-night] = dist[x][y][z][night] + 1
          q.append((nx, ny, z+1, 1-night))
    if dist[x][y][z][1-night] == 0:
      dist[x][y][z][1-night] = dist[x][y][z][night] + 1
      q.append((x, y, z, 1-night))
  
bfs(0 ,0, 0, 0)

answer = -1
for j in range(2):
  for i in range(l+1):
    if dist[n-1][m-1][i][j] == 0:
      continue
    if answer == -1 or answer > dist[n-1][m-1][i][j]:
      answer = dist[n-1][m-1][i][j]

print(answer)