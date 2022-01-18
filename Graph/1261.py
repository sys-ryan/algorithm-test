import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

d = [[-1] * m for _ in range(n)]
check = [[False] * m for _ in range(n)]

q = deque()
next_q = deque()

q.append((0, 0))
check[0][0] = True
d[0][0] = 0

while q:
  x, y = q.popleft()

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]

    if 0 <= nx < n and 0 <= ny < m:
      if check[nx][ny] == False:
        if d[nx][ny] == -1 and a[nx][ny] == 0:
          d[nx][ny] = d[x][y]
          check[nx][ny] = True
          q.append((nx, ny))
        elif d[nx][ny] == -1 and a[nx][ny] != 0:
          d[nx][ny] = d[x][y] + 1
          check[nx][ny] = True
          next_q.append((nx, ny))

  if not q:
    q = next_q
    next_q = deque()

print(d[n-1][m-1])

