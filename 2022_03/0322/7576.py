from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      q.append((i, j))
      check[i][j] = 0

while q:
  x, y, = q.popleft()

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if check[nx][ny] == -1 and a[nx][ny] == 0:
        check[nx][ny] = check[x][y] + 1
        q.append((nx, ny))

ok = True
for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and check[i][j] == -1:
      ok = False

if not ok:
  print(-1)
  exit()

answer = 0
for i in range(n):
  for j in range(m):
    if answer < check[i][j]:
      answer = check[i][j]

print(answer)