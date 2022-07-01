from collections import deque

n, m, start = map(int, input().split())
a = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  a[u][v] = a[v][u] = True

check = [False] * (n+1)
dfs_result = []
bfs_result = []

def dfs(start):
  global check
  check[start] = True
  dfs_result.append(start)

  for i in range(1, n+1):
    if a[start][i] and not check[i]:
      dfs(i)

def bfs(start):
  check = [False] * (n+1)
  bfs_result.append(start)

  q = deque()
  q.append(start)
  check[start] = True

  while q:
    x = q.popleft()

    for i in range(1, n+1):
      if a[x][i] and not check[i]:
        q.append(i)
        check[i] = True
        bfs_result.append(i)

dfs(start)
print(' '.join(map(str, dfs_result)))
bfs(start)
print(' '.join(map(str, bfs_result)))