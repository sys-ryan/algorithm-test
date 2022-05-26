import sys
n, m = map(int, input().split())
a = [list(map(str, list(input()))) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(x, y, px, py, color):
  if check[x][y]:
    return True

  check[x][y] = True
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if not (nx == px and ny == py) and a[nx][ny] == color:
        if go(nx, ny, x, y, color):
          return True

  return False

for i in range(n):
  for j in range(m):
    if not check[i][j]:
      if go(i, j, -1, -1, a[i][j]):
        print("Yes")
        sys.exit()

print("No")
