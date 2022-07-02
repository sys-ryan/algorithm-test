from collections import deque

n ,m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  dist[x][y] = 1

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < m:
        if dist[nx][ny] == -1 and maze[nx][ny] == 1:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))

bfs(0, 0)

print(dist[n-1][m-1])