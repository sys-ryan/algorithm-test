#Two Dots
import sys

n, m = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

d = [[-1] * m for _ in range(n)]
a = [list(input()) for _ in range(n)]

# ok = False
def go(x, y, cnt, color):
  if d[x][y] > -1:
    return cnt - d[x][y] >= 4
  
  d[x][y] = cnt
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == color:
        if go(nx, ny, cnt+1, color):
          return True

  return False


for i in range(n):
  for j in range(m):
    if d[i][j] == -1:
      if go(i, j, 0, a[i][j]):
        print("Yes")
        sys.exit(0)

print("No")

# for el in d:
#   print(el)
# print(d)
# print(a)
# print("Yes" if ok else "No")