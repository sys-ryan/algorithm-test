#서울 지하철 2호선 (순환선과의 거리)

import sys
sys.setrecursionlimit(1000000)
from collections import deque



n = int(input())
g = [[] for _ in range(n+1)]
check = [0] * (n+1) # 0: not visited, 1: visited, 2: cycle

for _ in range(1, n+1):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

for i in range(1, n+1):
  g[i].sort()

#p -> x
def go(x, p):
  # -2: found cycle and not included
  # -1: not found cycle
  # 0~n-1: foun ctycle and start index

  if check[x] == 1:
    return x
  
  check[x] = 1
  for y in g[x]:
    if y == p:
      continue
    
    res = go(y, x)

    if res == -2:
      return -2
    if res >= 0:
      check[x] = 2
      if x == res:
        return -2
      else:
        return res
  
  return -1


go(1, 0)

q = deque()
dist = [-1]*(n+1)

for i in range(1, n+1):
  if check[i] == 2:
    dist[i] = 0
    q.append(i)
  else:
    dist[i] = -1

while q:
  x = q.popleft()
  for y in g[x]:
    if dist[y] == -1:
      dist[y] = dist[x]+1
      q.append(y)

for i in range(1, n+1):
  print(dist[i], end=" ")
print()