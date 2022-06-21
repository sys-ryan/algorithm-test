def check(row, col):
  if check_col[col]:
    return False
  if check_dig[row+col]:
    return False
  if check_dig2[row-col+n-1]:
    return False
  return True

def calc(row):
  # row 행에 퀸을 어디에 놓을지 결정해야함
  if row == n:
    return 1
  ans = 0
  for col in range(n):
    if check(row, col):
      check_dig[row+col] = True
      check_dig2[row-col+n-1] = True
      check_col[col] = True
      # a[row][col] = True
      ans += calc(row+1)
      check_dig[row+col] = False
      check_dig2[row-col+n-1] = False
      check_col[col] = False
      # a[row][col] = False
  return ans

n = int(input())
# a = [[False]*n for _ in range(n)]
check_col = [False] * n # i th 열에 퀸이 놓여져 있으면 true
check_dig = [False] * (2*n - 1) # / 대각선에 퀸이 있으면 true
check_dig2 = [False] * (2*n - 1) # \ 대각선에 퀸이 있으면 true

print(calc(0))