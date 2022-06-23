n = int(input())
a = list(map(int, input().split()))

d1 = [0] * n
d2 = [0] * n

for i in range(n):
  d1[i] = 1
  for j in range(i):
    if d1[i] < d1[j] + 1 and a[j] < a[i]:
      d1[i] = d1[j] + 1
    
for i in range(n-1, -1, -1):
  d2[i] = 1
  for j in range(i, n):
    if d2[i] < d2[j] + 1 and a[i] > a[j]:
      d2[i] = d2[j] + 1

ans = 0
for i in range(n):
  if ans < d1[i] + d2[i] - 1:
    ans = d1[i] + d2[i] - 1

print(ans)