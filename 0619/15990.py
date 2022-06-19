t = int(input())

mod = 1000000009
d = [[0, 0, 0, 0] for _ in range(100001)]

d[1][1] = 1
d[1][2] = 0
d[1][3] = 0
d[2][1] = 0
d[2][2] = 1
d[2][3] = 0
d[3][1] = 1
d[3][2] = 1
d[3][3] = 1
d[4][1] = 2
d[4][2] = 0
d[4][3] = 1

for i in range(5, 100001):
  d[i][1] = d[i-1][2] + d[i-1][3]
  d[i][2] = d[i-2][1] + d[i-2][3]
  d[i][3] = d[i-3][1] + d[i-3][2]

  d[i][1] %= mod
  d[i][2] %= mod
  d[i][3] %= mod


for _ in range(t):
  n = int(input())
  print(sum(d[n]) % mod)