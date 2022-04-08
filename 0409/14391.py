n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

ans = 0

for s in range(1<<(n*m)):
  total = 0
  for i in range(n):
    cur = 0
    for j in range(m):
      k = i*m + j
      if (s&(1<<k)) == 0:
        cur = cur*10 + a[i][j]
      else:
        total += cur
        cur = 0
    total += cur
  for j in range(m):
    cur = 0
    for i in range(n):
      k = i*m + j
      if (s&(1<<k)) != 0:
        cur = cur*10 + a[i][j]
      else:
        total += cur
        cur = 0
    total += cur

  ans = max(ans, total)

print(ans)
