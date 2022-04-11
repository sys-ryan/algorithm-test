n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
s = ''

# 행이 홀수개
if n % 2 == 1:
  for i in range(n):
    if i % 2 == 0:
      s += 'R' * (m-1)
      if i != n-1:
        s += 'D'
    else:
      s += 'L' * (m-1)
      if i != n-1:
        s += 'D'

# 열이 홀수개
elif m % 2 == 1:
  for j in range(m):
    if j%2 == 0:
      s += 'D' * (n-1)
      if j != m-1:
        s += 'R'
    else:
      s += 'U' * (n-1)
      s += 'R'

# 행, 열 모두 짝수개
else:
  x = 0
  y = 1
  for i in range(n):
    for j in range(m):
      if (i+j) % 2 == 1: #검정칸
        if a[x][y] > a[i][j]:
          x, y, = i, j
        
  x1 = 0
  y1 = 0
  x2 = n-1
  y2 = m-1
  s2 = ''

  while x2 - x1 > 1:
    if x1//2 < x//2:
      s += 'R' * (m-1)
      s += 'D'
      s += 'L' * (m-1)
      s += 'D'
      x1 += 2 

    if x//2 < x2//2:
      s2 += 'R' * (m-1)
      s2 += 'D'
      s2 += 'L' * (m-1)
      s2 += 'D'
      x2 -= 2
    
  while y2 - y1 > 1:
    if y1//2 < y//2:
      s += 'DRUR'
      y1 += 2
    
    if y//2 < y2//2:
      s2 += 'DRUR'
      y2 -= 2

  if y == y1:
    s += 'RD'
  else:
    s += 'DR'

  s += s2[::-1]

print(s)  