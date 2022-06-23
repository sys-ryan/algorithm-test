n = int(input())
a = list(map(int, input().split()))
d = [0] * (n)

for i in range(n-1, -1, -1):
  d[i] = 1
  for j in range(i, n):
    if d[i] < d[j] + 1 and a[i] > a[j]:
      d[i] = d[j] + 1

print(max(d))
