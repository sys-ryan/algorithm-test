import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())

for _ in range(t):
  l = int(input())

  d = [[-1] * l for _ in range(l)]
  sx, sy = map(int, input().split())
  es, ey = map(int, input().split())

  q = deque()
  q.append((sx, sy))
  d[sx][sy] = 0
  while q:
    x, y = q.popleft()
  
    for k in range(8):
      nx, ny = x+dx[k], y+dy[k]
      
      if 0 <= nx < l and 0 <= ny < l:
        if d[nx][ny] == -1:
          d[nx][ny] = d[x][y] + 1
          q.append((nx, ny))

  print(d[es][ey])  
