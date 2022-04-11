from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  check[x][y] = 1

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if check[nx][ny] == 0 and a[nx][ny] == 1:
          check[nx][ny] = check[x][y] + 1
          q.append((nx, ny))

bfs(0, 0)
print(check[n-1][m-1])
