from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * n for _ in range(n)]
group = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def set_group():
  cnt = 0

  for i in range(n):
    for j in range(n):
      if a[i][j] == 1 and group[i][j] == 0:
        cnt += 1
        group[i][j] = cnt

        q = deque()
        q.append((i, j))

        while q:
          x, y = q.popleft()
          for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
              if a[nx][ny] == 1 and group[nx][ny] == 0:
                group[nx][ny] = cnt
                q.append((nx, ny))

def calc_bridge():
  q = deque()
  for i in range(n):
    for j in range(n):
      if a[i][j] == 1:
        q.append((i, j))
        dist[i][j] = 0

  while q:
    x, y = q.popleft()

    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < n:
        if dist[nx][ny] == -1:
          group[nx][ny] = group[x][y]
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))

  ans = -1
  for i in range(n):
    for j in range(n):
      for k in range(4):
        x, y, = i+dx[k], j+dy[k]

        if 0 <= x < n and 0 <= y < n:
          if group[i][j] != group[x][y]:
            if ans == -1 or ans > dist[i][j] + dist[x][y]:
              ans = dist[i][j] + dist[x][y]

  return ans


set_group()
print(calc_bridge())