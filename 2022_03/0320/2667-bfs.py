# 2667 bfs
import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
from collections import deque

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

d = [[0] * n for _ in range(n)]

def bfs(x, y, cnt):
  q = deque()
  q.append((x, y))
  d[x][y] = cnt

  while q:
    x, y, = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]

      if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != 0 and d[nx][ny] == 0:
          d[nx][ny] = cnt
          q.append((nx, ny))

cnt = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and d[i][j] == 0:
      cnt += 1
      bfs(i, j, cnt)

print(cnt)

ans = [0] * (cnt+1)
for i in range(n):
  for j in range(n):
    for k in range(1, cnt+1):
      if d[i][j] == k:
        ans[k] += 1

ans.sort()

for i in range(1, cnt+1):
  print(ans[i])