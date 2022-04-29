# 3085 efficient version
# 틀렸습니다 

def horizontal_change_check(a, sx, sy, ex, ey):
  n = len(a)
  ans = 1
  # horizontal check
  cnt = 1
  for i in range(1, n):
    if a[sx][i] == a[ex][i-1]:
      cnt += 1
    else:
      cnt = 1

    if ans < cnt:
      ans = cnt
  
  # vertical check:
  for i in range(sy, ey+1):
    cnt = 1
    for j in range(1, n):
      if a[j][i] == a[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      
      if ans < cnt:
        ans = cnt

  return ans

def vertical_change_check(a, sx, sy, ex, ey):
  n = len(a)
  ans = 1

  # vertical check
  cnt = 1
  for i in range(1, n):
    if a[i][sy] == a[i-1][ey]:
      cnt += 1
    else:
      cnt = 1
    
    if ans < cnt:
      ans = cnt
  
  # horizontal check:
  for i in range(sx, ex+1):
    cnt = 1
    for j in range(1, n):
      if a[i][j] == a[i][j-1]:
        cnt += 1
      else:
        cnt = 1
    
    if ans < cnt:
      ans = cnt

  return ans

n = int(input())
a = [list(map(str, input())) for _ in range(n)]

ans = 0
for i in range(n):
  for j in range(n):
    if j+1 < n:
      a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
      temp = horizontal_change_check(a, i, j, i, j+1)
      if ans < temp:
        ans = temp
      a[i][j], a[i][j+1] = a[i][j+1], a[i][j]

    if i+1 < n:
      a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
      temp = vertical_change_check(a, i, j, i+1, j)
      if ans < temp:
        ans = temp
      a[i][j], a[i+1][j] = a[i+1][j], a[i][j]

print(ans)