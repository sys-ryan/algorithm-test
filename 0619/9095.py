t = int(input())
d = [0] * 12

d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(5, 12):
  d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(t):
  n = int(input())
  print(d[n])