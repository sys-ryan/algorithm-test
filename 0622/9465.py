



t = int(input())
for _ in range(t):
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(2)]

  d = [[0]*3 for _ in range(n+1)]

  d[0][0] = 0
  d[0][1] = a[0][0]
  d[0][2] = a[1][0]

  for i in range(1, n):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = max(d[i-1][0], d[i-1][2]) + a[0][i]
    d[i][2] = max(d[i-1][0], d[i-1][1]) + a[1][i]

  print(max(d[n-1]))
    


