from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

group = [[-1] * m for _ in range(n)]
group_size = []

def bfs(sx, sy):
  g = len(group_size)
  q = deque()
  q.append((sx, sy))
  group[sx][sy] = g
  check[sx][sy] = True
  cnt = 1

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if not check[nx][ny] and a[nx][ny] == 0:
          group[nx][ny] = g
          check[nx][ny] = True
          q.append((nx, ny))
          cnt += 1
  
  group_size.append(cnt)

for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and not check[i][j]:
      bfs(i, j)

for i in range(n):
  for j in range(m):
    if a[i][j] == 0:
      print(0, end='')
    else:
      near = set()
      for k in range(4):
        nx, ny = i+dx[k], j+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
          if a[nx][ny] == 0:
            near.add(group[nx][ny])
        
      answer = 1
      for g in near:
        answer += group_size[g]
      print(answer % 10, end='')
  
  print()
