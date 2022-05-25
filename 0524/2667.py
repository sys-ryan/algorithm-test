from collections import deque


n = int(input())
a = []
b = [[0]*n for _ in range(n)]
for _ in range(n):
  a.append(list(map(int, input())))

check = [[False]*n for _ in range(n)]

def bfs(x, y, cnt):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  q = deque()

  check[x][y] = True
  q.append((x, y))
  b[x][y] = cnt

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] == 1 and not check[nx][ny]:
          check[nx][ny] = True
          q.append((nx, ny))
          b[nx][ny] = cnt

cnt = 1
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and b[i][j] == 0:
      bfs(i, j, cnt)
      cnt += 1

ans = []
for k in range(1, cnt):
  total = 0
  for i in range(n):
    for j in range(n):
      if b[i][j] == k:
        total += 1

  ans.append(total)

print(cnt-1)
ans.sort()
for el in ans:
  print(el)