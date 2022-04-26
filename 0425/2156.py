n = int(input())
a = [int(input()) for _ in range(n)]

d = [0] * (n)

if n == 1:
  print(a[0])
  exit()
elif n == 2:
  print(a[0]+a[1])
  exit()

d[0] = a[0]
d[1] = a[0] + a[1]

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + a[i], d[i-3] + a[i-1] + a[i])

print(d[n-1])