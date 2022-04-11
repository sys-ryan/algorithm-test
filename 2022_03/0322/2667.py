import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n = int(input()) 

a = [list(map(int,input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

def dfs(x, y, cnt):
  check[x][y] = cnt

  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < n and 0 <= ny < n:
      if check[nx][ny] == 0 and a[nx][ny] != 0:
        dfs(nx, ny, cnt)

cnt = 0
for i in range(n):
  for j in range(n):
    if a[i][j] != 0 and check[i][j] == 0:
      cnt += 1
      dfs(i, j, cnt)

print(cnt)

houses = []
for k in range(1, cnt+1):
  h = 0
  for i in range(n):
    for j in range(n):
      if k == check[i][j]:
        h += 1
  houses.append(h)

houses.sort()
for h in houses:
  print(h)