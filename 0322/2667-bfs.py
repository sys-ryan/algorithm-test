from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

def bfs(x, y, cnt):
  q = deque()
  q.append((x, y))
  check[x][y] = cnt

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if check[nx][ny] == 0 and a[nx][ny] != 0:
          check[nx][ny] = cnt
          q.append((nx, ny))


cnt = 0
for i in range(n):
  for j in range(n):
    if a[i][j] != 0 and check[i][j] == 0:
      cnt += 1
      bfs(i, j, cnt)


print(cnt)

ans = [0] * (cnt+1)

for i in range(n):
  for j in range(n):
    for k in range(1, cnt+1):
      if check[i][j] == k:
        ans[k] += 1

ans.sort()

for i in range(1, cnt+1):
  print(ans[i])