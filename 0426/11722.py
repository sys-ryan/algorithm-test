n = int(input())
a = list(map(int, input().split()))

d = [[0]*n for _ in range(n)]

for i in range(n-1, -1, -1):
  d[i] = 1
  for j in range(i+1, n):
    if a[i] > a[j] and d[i] < d[j] + 1:
      d[i] = d[j] + 1

print(max(d))