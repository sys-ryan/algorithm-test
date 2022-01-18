import sys

n = int(input())
a = list(map(int, input().split()))

f = [0] * 1000001

for i in range(0, n):
  f[a[i]] += 1

s = [0]
ans = [0] * n
for i in range(1, n):
  # print(s)
  while s and f[a[i]] > f[a[s[-1]]]:
    ans[s[-1]] = a[i]
    s.pop()
  s.append(i)

for el in s:
  ans[el] = -1

print(' '.join(map(str, ans)))


