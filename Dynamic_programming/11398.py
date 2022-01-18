#연속합 2
import sys
input = sys.stdin.readline

n = int(input())

a = '-1001 ' + input()
a = list(map(int, a.split()))

d1 = [-1001] * (n+1)
d2 = [-1001] * (n+1)

for i in range(1, n+1):
  d1[i] = a[i]
  if i == 1:
    continue
  if d1[i] < d1[i-1] + a[i]:
    d1[i] = d1[i-1] + a[i]

for i in range(n, 0, -1):
  d2[i] = a[i]
  if i == n:
    continue
  if d2[i] < d2[i+1] + a[i]:
    d2[i] = d2[i+1] + a[i]
  
ans = max(d1)

for i in range(2, n):
  if ans < d1[i-1] + d2[i+1]:
    ans = d1[i-1]+ d2[i+1]

print(ans)