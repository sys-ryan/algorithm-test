import sys

mod = 10007
n = int(input())
d = [0] * (n+1)

if n <= 3:
  if n == 1:
    print(1)
  elif n == 2:
    print(3)
  elif n == 3:
    print(5)
  sys.exit()

d[1] = 1
d[2] = 3
d[3] = 5

for i in range(4, n+1):
  d[i] = d[i-1] + 2*d[i-2]

print(d[n] % 10007)
