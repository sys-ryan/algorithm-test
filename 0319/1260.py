from collections import deque

n, m, start = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

for i in range(1, n+1):
  g[i].sort()

check = [False] * (n+1)

def dfs(x):
  check[x] = True
  print(x, end=' ')

  for y in g[x]:
    if check[y] == False:
      dfs(y)

def bfs(start):
  check = [False] * (n+1)
  q = deque()

  q.append(start)
  check[start] = True

  while q:
    x = q.popleft()
    print(x, end=' ')

    for y in g[x]:
      if check[y] == False:
        check[y] = True
        q.append(y)
      
dfs(start)
print()
bfs(start)
print()