#숨바꼭질 4
import sys
sys.setrecursionlimit(1000000)
from collections import deque

MAX = 2000001
d = [-1] * MAX
check = [False] * MAX
v = [-1] * MAX

n, k = map(int, input().split())

q = deque()
q.append(n)
d[n] = 0
check[n] = True

def go(n, m):
  if n != m:
    go(n, v[m])
  print(m, end=' ')

while q:
  x = q.popleft()

  if x-1 >= 0 and not check[x-1]:
    d[x-1] = d[x] + 1
    q.append(x-1)
    check[x-1] = True
    v[x-1] = x

  if x+1 < MAX and not check[x+1]:
    d[x+1] = d[x] + 1
    q.append(x+1)
    check[x+1] = True
    v[x+1] = x
  
  if x*2 < MAX and not check[x*2]:
    d[x*2] = d[x] + 1
    q.append(2*x)
    check[x*2] = True
    v[x*2] = x

print(d[k])
go(n, k)
print()





