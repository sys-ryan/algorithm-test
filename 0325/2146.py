# 미완성 - 수정 필요 

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * n for _ in range(n)]
group = [[0] * n for _ in range(n)]
# check = [[False] * n for _ in range(n)]

def assign_group(x, y, group_number):
  q = deque()
  q.append((x, y))
  dist[x][y] = 0
  group[x][y] = group_number

  while q:
    x, y = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] == 1 and group[nx][ny] == 0:
          group[nx][ny] = group[x][y]
          dist[x][y] = 0
          q.append((nx, ny))
          
group_number = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and group[i][j] == 0:
      group_number += 1
      assign_group(i, j, group_number)

def calc_dist():
  q = deque()
  for i in range(n):
    for j in range(n):
      if a[i][j] == 1:
        q.append((i, j))
  
  while q:
    x, y = q.popleft()
    
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      
      if 0 <= nx < n and 0 <= ny < n:
        if dist[nx][ny] == -1:
          dist[nx][ny] = dist[x][y] + 1
          group[nx][ny] = group[x][y]
          q.append((nx, ny))

calc_dist()


def get_shortest_path():
  min_dist = -1
  for i in range(n):
    for j in range(n):
      for k in range(4):
        nx, ny = i+dx[k], j+dy[k]

        if 0 <= nx < n and 0 <= ny < n:
          if group[i][j] != group[nx][ny]:
            if min_dist == -1 or min_dist > dist[i][j] + dist[nx][ny]:
              min_dist = dist[i][j] + dist[nx][ny]
              print(min_dist)

  return min_dist

print(get_shortest_path())



for el in dist:
  print(el)


