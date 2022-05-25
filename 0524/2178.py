from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

check = [[False]*m for _ in range(n)]
d = [[0] * m for _ in range(n)]

def bfs(x, y):
  q = deque()
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]

  q.append((x, y))
  check[x][y] = True
  d[x][y] = 1

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < m:
        if not check[nx][ny] and a[nx][ny] == 1:
          q.append((nx, ny))
          check[nx][ny] = True
          d[nx][ny] = d[x][y] + 1

bfs(0, 0)
print(d[n-1][m-1])