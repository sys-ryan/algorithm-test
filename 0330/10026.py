from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
a = [list(map(str, input())) for _ in range(n)]

check = [[False] * n for _ in range(n)]

def can(blind, u, v):
  if u == v:
    return True

  if blind:
    if u == 'R' and v == 'G':
      return True
    if u == 'G' and v == 'R':
      return True

  return False

def bfs(x, y, blind=False):
  q = deque()
  q.append((x, y))
  check[x][y] = True

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < n:
        if check[nx][ny]:
          continue
        if can(blind, a[x][y], a[nx][ny]):
          check[nx][ny] = True
          q.append((nx, ny))


answer = 0
for i in range(n):
  for j in range(n):
    if check[i][j] == False:
      answer += 1
      bfs(i, j)

check = [[False] * n for _ in range(n)]
answer_blind = 0
for i in range(n):
  for j in range(n):
    if check[i][j] == False:
      answer_blind += 1
      bfs(i, j, True)

print(f'{answer} {answer_blind}')