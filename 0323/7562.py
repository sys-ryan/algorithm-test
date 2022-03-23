from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

t = int(input())

def bfs(x, y, cnt):
  q = deque()
  check[x][y] = cnt
  q.append((x, y))

  while q:
    x, y = q.popleft()

    for k in range(8):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if check[nx][ny] == 0:
          check[nx][ny] = check[x][y] + 1
          q.append((nx, ny))

for _ in range(t):
  n = int(input())

  check = [[0] * n for _ in range(n)]
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())

  if sx == ex and sy == ey:
    print(0)
  else:
    cnt = 0
    bfs(sx, sy, cnt)

    print(check[ex][ey])