#오큰수 

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

s = [0]
ans = [0] * n

for i in range(n):
  if not s:
    s.append(i)
  while s and a[s[-1]] < a[i]:
    ans[s.pop()] = a[i]
  s.append(i)

while s:
  ans[s.pop()] = -1

print(" ".join(map(str, ans)))
