import sys

n = int(input())
m = int(input())
broken = [False] * (10)
b = list(map(int, input().split()))
for i in range(m):
  broken[b[i]] = True

maxval = 1000001

def possible(n):
  if n == 0:
    if broken[0]:
      return 0
    else:
      return 1
  
  length = 0
  while n > 0:
    if broken[n%10]:
      return 0
    length += 1
    n = n // 10
  
  return length


ans = abs(n-100)

for i in range(maxval):
  c = i
  length = possible(c)
  if length > 0:
    press = abs(n-c)

    if ans > length + press:
      ans = length + press

print(ans)
