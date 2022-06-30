from collections import deque 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, mn, mx): # mn <= 방문하는 수의 크기 <= mx
  if mn > a[0][0] or mx < a[0][0]:
    return False

  n = len(a)
  c = [[False]*n for _ in range(n)]

  q = deque()
  q.append((0, 0))
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
  mid = (left+right)//2
  if go(a, mid):
    right = mid-1
    ans = min(ans, mid)
  else:
    left = mid+1
print(ans)