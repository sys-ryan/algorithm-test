import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, mn, mx):
  if mn > a[0][0] or mx < a[0][0]:
    return False

  n = len(a)
  c = [[False]*n for _ in range(n)]
  q = deque()
  q.append((0, 0))

  c[0][0] = True
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx = x+dx[k]
      ny = y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if c[nx][ny] == False and mn <= a[nx][ny] <= mx:
          q.append((nx, ny))
          c[nx][ny] = True
  return c[n-1][n-1]

def go(a, diff):
  for mn in range(200-diff+1):
    if bfs(a, mn, mn+diff):
      return True
  return False

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

left = 0
right = 200
ans = 200

while left <= right:
  mid = (left + right) // 2
  if go(a, mid):
    right = mid - 1
    ans = min(ans, mid)
  else:
    left = mid + 1
  
print(ans)