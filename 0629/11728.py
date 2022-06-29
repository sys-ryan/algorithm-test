n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * (n+m)
i = 0
j = 0
k = 0

while i < n and j < m:
  if a[i] <= b[j]:
    c[k] = a[i]
    k += 1
    i += 1
  else:
    c[k] = b[j]
    k += 1
    j += 1

while i < n:
  c[k] = a[i]
  k += 1
  i += 1

while j < m:
  c[k] = b[j]
  k += 1
  j += 1

for i in range(n+m):
  print(c[i], end=' ')
print()