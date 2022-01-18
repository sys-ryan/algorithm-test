import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

n, m = map(int, input().split())

d = [[0] * (m+1) for _ in range(n+1)]
a = [list(map(int, list(input()))) for _ in range(n)]

def bfs(sx, sy, cnt):
  q.append((sx, sy))
  d[sx][sy] = cnt

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x + dx[k], y+dy[k]
      
      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 1 and d[nx][ny] == 0:
          d[nx][ny] = d[x][y] + 1
          q.append((nx, ny))


bfs(0, 0, 1)
print(d[n-1][m-1])

