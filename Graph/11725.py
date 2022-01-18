#트리의 부모 찾기 

import sys
from collections import deque

n = int(input())
parent = [0] * (n+1)
g = [[] for _ in range(n+1)]
check = [False] * (n+1)
# depth = [0] * (n+1)


for i in range(n-1):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

# depth[1] = 0
check[1] = True
q = deque()
q.append(1)
parent[1] = 0

while q:
  x  = q.popleft()
  for y in g[x]:
    if check[y] == False:
      # depth[y] = depth[x] + 1
      check[y] = True
      parent[y] = x
      q.append(y)

for i in range(2, n+1):
  print(parent[i])


