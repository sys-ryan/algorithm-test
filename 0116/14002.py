import sys

n = int(input())
a = list(map(int, input().split()))

d = [0] * n
f = [-1] * n

for i in range(n):
  d[i] = 1

  for j in range(i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
      f[i] = j
  
max_val = max(d)
print(max_val)

def go(n):
  if n == -1:
    return
  go(f[n])
  print(a[n], end=' ')

idx = 0
for i in range(n):
  if d[i] == max_val:
    idx = i

go(idx)
print()