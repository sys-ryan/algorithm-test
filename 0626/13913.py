from collections import deque
import sys

MAX = 200000

check = [False] * (MAX+1)
dist = [-1] * (MAX+1)
via = [-1] * (MAX+1)

n, m = map(int, input().split())
q = deque()
check[n] = True
dist[n] = 0
q.append(n)

while q:
  x = q.popleft()
  for y in [x-1, x+1, x*2]:
    if 0 <= y < MAX and not check[y]:
      q.append(y)
      dist[y] = dist[x] + 1
      check[y] = True
      via[y] = x
  
print(dist[m])

res = [m]
while via[m] != via[n]:
  res.append(via[m])
  m = via[m]
# res.append(m)
res.reverse()
print(' '.join(map(str, res)))


