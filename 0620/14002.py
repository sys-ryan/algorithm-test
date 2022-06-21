n = int(input())
a = [0] + list(map(int, input().split()))

d = [0] * (n+1)
v = [0] * (n+1)

for i in range(1, n+1):
  d[i] = 1

  for j in range(1, i):
    if d[i] < d[j] + 1 and a[j] < a[i]:
      d[i] = d[j] + 1
      v[i] = j

def go(p):
  # print(f'p, a[p]: {p}, {a[p]}')
  if p == 0:
    return
  
  go(v[p])
  print(a[p], end=' ')

max_idx = 0
max_val = 0
for i in range(len(d)):
  if max_val < d[i]:
    max_val = d[i]
    max_idx = i

print(max_val)
go(max_idx)
print()