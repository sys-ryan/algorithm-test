import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [-1001] * n
dr = [-1001] * n

if n == 1:
  print(a[0])
  sys.exit(0)

for i in range(n):
  d[i] = a[i]
  if i == 0:
    continue
  if d[i] < d[i-1] + a[i]:
    d[i] = d[i-1] + a[i]
  


for i in range(n-1, -1, -1):
  dr[i] = a[i]
  if i == n-1:
    continue
  if dr[i] < dr[i+1] + a[i]:
    dr[i] = dr[i+1] + a[i]

ans = max(d)

for i in range(n):
  if i == 0:
    ans = max(ans, dr[i+1])
  elif i == n-1:
    ans = max(ans, d[i-1])
  else:
    ans = max(ans, d[i-1] + dr[i+1])
  
print(ans)