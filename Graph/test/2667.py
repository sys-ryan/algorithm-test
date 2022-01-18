from locale import D_FMT
import sys
from collections import deque

q = deque()
n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# check = [[False] * n for _ in range(n)]
d = [[0] * n for _ in range(n)]
cnt = 0

def bfs(x, y, cnt):

  d[x][y] = cnt
  q.append((x, y))
  

  while q:
    x, y = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] == 1 and d[nx][ny] == 0:
          d[nx][ny] = cnt
          q.append((nx, ny))
          
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and d[i][j] == 0:
      cnt += 1
      bfs(i, j, cnt)

print(cnt)

ans = []
for k in range(1, cnt+1):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if d[i][j] == k:
        cnt += 1

  ans.append(cnt)

ans.sort()
for el in ans:
  print(el)


      
