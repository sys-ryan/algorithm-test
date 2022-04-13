STAR = '*'
BLANK = ' '

def go(a, x, y, n, color):
  if color == BLANK:
    for i in range(x, x+n):
      for j in range(y, y+n):a[i][j] = BLANK
  else:
    if n == 1:
      a[x][y] = STAR
    else:
      newColor = STAR
      m = n//3
      for i in range(3):
        for j in range(3):
          if i == 1 and j == 1:
            newColor = BLANK
          else:
            newColor = STAR
          go(a, x+m*i, y+m*j, m, newColor)

n = int(input())
a = [[BLANK] * n for _ in range(n)]
go(a, 0, 0, n, STAR)
for row in a:
  print(''.join(row))