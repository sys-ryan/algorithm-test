from collections import deque 

q = deque()

d = [[-1]*201 for _ in range(201)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
sx, sy, ex, ey = map(int, input().split())

q.append((sx, sy))
d[sx][sy] = 0

while q:
  x, y = q.popleft()

  for k in range(6):
    nx, ny = x+dx[k], y+dy[k]

    if 0 <= nx < n and 0 <= ny < n:
      if d[nx][ny] == -1:
        q.append((nx, ny))
        d[nx][ny] = d[x][y] + 1

print(d[ex][ey])