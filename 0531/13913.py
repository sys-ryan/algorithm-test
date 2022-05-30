from collections import deque
import sys
MAX = 2000001

sys.setrecursionlimit(100000)

check = [False] * MAX
dist = [-1] * MAX
via = [-1] * MAX

n, m = map(int, input().split())

check[n] = True
dist[n] = 0
q = deque()
q.append(n)

while q:
  x = q.popleft()

  if x-1 >= 0 and not check[x-1]:
    q.append(x-1)
    dist[x-1] = dist[x] + 1
    check[x-1] = True
    via[x-1] = x
  
  if x+1 < MAX and not check[x+1]:
    q.append(x+1)
    dist[x+1] = dist[x] + 1
    check[x+1] = True
    via[x+1] = x

  if x*2 < MAX and not check[x*2]:
    q.append(x*2)
    dist[x*2] = dist[x] + 1
    check[x*2] = True
    via[x*2] = x

print(dist[m])

def go(n, m):
  if n != m:
    go(n, via[m])
  print(m, end=' ')

go(n, m)