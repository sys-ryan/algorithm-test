#오등큰수 

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = [0]*n
s = [0]

freq = [0]*1000001

for i in range(n):
  freq[a[i]] += 1

for i in range(1, n):
  if not s:
    s.append(i)
  while s and freq[a[s[-1]]] < freq[a[i]]:
    ans[s.pop()] = a[i] 
  s.append(i)

while s: 
  ans[s.pop()] = -1

print(' '.join(map(str, ans)))
