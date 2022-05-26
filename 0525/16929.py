import sys

n, m = map(int, input().split())
a = [list(map(str, list(input()))) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(x, y, cnt, color):
  if check[x][y] == True:
    return cnt - dist[x][y] >= 4
  
  check[x][y] = True
  dist[x][y] = cnt

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]

    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == color:
        if go(nx, ny, cnt+1, color):
          return True

  return False

ok = False
for i in range(n):
  for j in range(m):
    if not check[i][j]:
      if go(i, j, 0, a[i][j]):
        print("Yes")
        sys.exit()
      
print("No")
