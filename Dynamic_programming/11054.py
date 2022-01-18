#가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

n = int(input())

d1 = [0] * (n+1)
d2 = [0] * (n+1)

a = '0 ' + input()
a = list(map(int, a.split()))

for i in range(1, n+1):
  d1[i] = 1
  for j in range(1, i):
    if a[j] < a[i] and d1[i] < d1[j] + 1:
      d1[i] = d1[j] + 1

for i in range(n, 0, -1):
  d2[i] = 1
  for j in range(n, i-1, -1):
    if a[i] > a[j] and d2[i] < d2[j] + 1:
      d2[i] = d2[j] + 1

ans = 0  
for i in range(1, n+1):
  if ans < d1[i] + d2[i] - 1:
    ans = d1[i] + d2[i] - 1

print(ans)

