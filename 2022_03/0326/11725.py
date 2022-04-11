from collections import deque

n = int(input())
parent = [0] * (n+1)
g = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(n-1):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

for i in range(1, n+1):
  g[i].sort()


check[1] = True
parent[1] = 0
q = deque()
q.append(1)

while q:
  x = q.popleft()
  for y in g[x]:
    if check[y] == False:
      check[y] = True
      parent[y] = x
      q.append(y)

for i in range(2, n+1):
  print(parent[i])