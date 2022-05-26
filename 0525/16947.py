import sys
from collections import deque

sys.setrecursionlimit(1000000)

n = int(input())
g = [[] for _ in range(n+1)]

for _ in range(n):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

check = [0] * (n+1)

def go(x ,p):
  # -2: cycle found, not included
  # -1: cycle not found
  # 0 ~ n: cycle found, starting index 

  if check[x]:
    return x
  
  check[x] = 1 # visited, not a cycle node
  for y in g[x]:
    if y == p:
      continue
    res = go(y, x)

    if res == -2:
      return -2
    
    if res >= 0:
      check[x] = 2 # visited, a cycle node
      if x == res:
        return -2
      else:
        return res
  
  return -1

go(1, -1)

dist = [-1] * (n+1)
q = deque()

# print(check)
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
      q.append(y)
      dist[y] = dist[x] + 1

print(' '.join(map(str, dist[1:])))