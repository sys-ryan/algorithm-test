BLANK = ' '
STAR = '*'

def go(a, x, y, n, color):
  if color == BLANK:
    m = 2*n-1
    for i in range(x, x+n):
      for j in range(m):
        a[i][j+i-x+y] = BLANK
      m -= 2
  elif color == STAR:
    if n != 1:
      m = n//2
      go(a, x, y, m, STAR)
      go(a, x+m, y-m, m, STAR)
      go(a, x+m, y+m, m, STAR)

      if n == 3:
        go(a, x+1, y, 1, BLANK)
      else:
        go(a, x+m, y-m+1, m, BLANK)

n = int(input())
a = [[STAR] * (2*n) for _ in range(n)]
go(a, 0, n-1, n, STAR)

for i in range(n):
  for j in range(n-i-1):
    a[i][j] = BLANK
    a[i][2*n-j-2] = BLANK
  a[i][2*n-1] = BLANK

for row in a:
  print(''.join(row))