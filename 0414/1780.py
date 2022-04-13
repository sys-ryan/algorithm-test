def smae(a, x, y, n):
  for i in range(x, x+n):
    for j in range(y, y+n):
      if a[x][y] != a[i][j]:
        return False
  return True

def solve(a, cnt, x, y, n):
  if smae(a, x, y, n):
    cnt[a[x][y] + 1] += 1 # cnt[0]: -1, cnt[1]: 0, cnt[2]: 1
    return
  m = n // 3
  for i in range(3):
    for j in range(3):
      solve(a, cnt, x + i*m, y + j*m, m)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * 3
solve(a, cnt, 0, 0, n)
for c in cnt:
  print(c)