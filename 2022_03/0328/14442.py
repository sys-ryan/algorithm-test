from collections import deque

n, m, l = map(int, input().split())
dist = [[[0] * 11 for _ in range(m)] for _ in range(n)]
a = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
  q = deque()
  dist[x][y][z] = 1
  q.append((x, y, z))

  while q:
    x, y, z = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
          dist[nx][ny][z] = dist[x][y][z] + 1
          q.append((nx, ny, z))
        if z+1 <= l and a[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
          dist[nx][ny][z+1] = dist[x][y][z] + 1
          q.append((nx, ny, z+1))


bfs(0, 0, 0)

answer = -1
for i in range(l+1):
  if dist[n-1][m-1][i] == 0:
    continue
  if answer == -1 or answer > dist[n-1][m-1][i]:
    answer = dist[n-1][m-1][i]

print(answer)


