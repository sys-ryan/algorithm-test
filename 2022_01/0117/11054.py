import sys

n = int(input())
a = list(map(int, input().split()))

d = [0] * n
dr = [1] * n

for i in range(n):
  d[i] = 1
  for j in range(i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1

for i in range(n-1, -1, -1):
  for j in range(n-1, i, -1):
    if a[j] < a[i] and dr[i] < dr[j] + 1:
      dr[i] = dr[j] + 1

ans = [0] * n
for i in range(n):
  ans[i] = d[i] + dr[i] - 1

print(max(ans))
  