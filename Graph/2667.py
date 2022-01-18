#단지번호붙이기 
import sys

# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[0] * n for _ in range(n)]
cnt = 0

def dfs(x, y, cnt):
  group[x][y] = cnt
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < n and 0 <= ny < n:
      if a[nx][ny] == 1 and group[nx][ny] == 0:
        dfs(nx, ny, cnt)
  

for i in range(n):
  for j in range(n):
    if a[i][j] == 1 and group[i][j] == 0:
      cnt += 1
      dfs(i, j, cnt)


print(cnt)

ans = [[0] for _ in range(cnt)]
for k in range(1, cnt+1):
  total = 0
  for i in range(n):
    for j in range(n):
      if group[i][j] == k:
        total += 1

  ans[k-1] = total

ans.sort()
for el in ans:
  print(el)