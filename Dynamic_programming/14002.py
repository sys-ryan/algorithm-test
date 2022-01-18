#가장 긴 증가하는 부분 수열4 (back tracking)
import sys

input = sys.stdin.readline

n = int(input())
a = '0 '
a += input()

a = list(map(int, a.split()))

d = [0] * (n+1)
v = [0] * (n+1)

for i in range(1, n+1):
  d[i] = 1
  for j in range(i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
      v[i] = j

ans = max(d)
ans_idx = 0
for i in range(1, n+1):
  if d[i] == ans:
    ans_idx = i
    break

def go(p):
  if p == 0:
    return
  go(v[p])
  print(a[p], end=" ")

print(ans)
go(ans_idx)
print()