n = int(input())
a = [0] + list(map(int, input().split()))

d = [0] * (n+1)

d[0] = 0
d[1] = a[1]

for i in range(2, n+1):
  for j in range(1, i+1):
    if d[i] < d[i-j] + a[j]:
      d[i] = d[i-j] + a[j]

print(d[n])