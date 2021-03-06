from collections import deque

n, m, start = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

for i in range(n+1):
  g[i].sort()

check = [False] * (n+1)
dfs_result = []
bfs_result = []

def dfs(start):
  global check
  check[start] = True
  dfs_result.append(start)

  for nxt in g[start]:
    if not check[nxt]:
      dfs(nxt)

def bfs(start):
  check = [False] * (n+1)
  q = deque()
  check[start] = True
  q.append(start)
  
  bfs_result.append(start)

  while q:
    x = q.popleft()

    for nxt in g[x]:
      if not check[nxt]:
        check[nxt] = True
        bfs_result.append(nxt)
        q.append(nxt)


dfs(start)
bfs(start)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))



