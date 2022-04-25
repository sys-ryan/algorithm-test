n = int(input())
a = list(map(int, input().split()))

d = [0] * n
v = [-1] * n

for i in range(n):
  d[i] = 1
  for j in range(i):
    if a[i] > a[j] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
      v[i] = j
  
def go(p):
  if p == -1:
    return
  
  go(v[p])
  print(a[p], end=' ')

max = 0
max_idx = 0
for i in range(n):
  if max < d[i]:
    max = d[i]
    max_idx = i

print(max)
go(max_idx)
print()