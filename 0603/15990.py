mod = 1000000009

t = int(input())

d = [[0, 0, 0, 0] for _ in range(100001)]

for i in range(1, 100001):

  if i-1 >= 0:
    d[i][1] = d[i-1][2] + d[i-1][3]

    if i == 1:
      d[i][1] = 1
  
  if i-2 >= 0:
    d[i][2] = d[i-2][1] + d[i-2][3]

    if i == 2:
      d[i][2] = 1
  
  if i-3 >= 0:
    d[i][3] = d[i-3][1] + d[i-3][2]

    if i == 3:
      d[i][3] = 1

  d[i][1] %= mod
  d[i][2] %= mod
  d[i][3] %= mod

for _ in range(t):
  n = int(input())

  print(sum(d[n]) % mod)