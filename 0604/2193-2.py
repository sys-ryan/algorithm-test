# 1 차원 다이나믹 

d = [0] * (91)
n = int(input())

d[1] = 1
d[2] = 1

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])