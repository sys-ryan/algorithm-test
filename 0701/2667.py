from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
result = [[0]*n for _ in range(n)]

q = deque()
check = [[False] * n for _ in range(n)]

def bfs(sx, sy, number):
  check[sx][sy] = True
  result[sx][sy] = number
  q.append((sx, sy))

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < n:
        if not check[nx][ny] and a[nx][ny] == 1:
          result[nx][ny] = number
          check[nx][ny] = True
          q.append((nx, ny))

number = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and not check[i][j]:
      number += 1
      bfs(i, j, number)

print(number)

number_count = []

for i in range(1, number+1):
  count = 0
  for j in range(n):
    for k in range(n):
      if result[j][k] == i:
        count += 1

  number_count.append(count)
number_count.sort()
for el in number_count:
  print(el)