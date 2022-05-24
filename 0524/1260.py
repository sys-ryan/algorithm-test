from collections import deque 

n, m, v = map(int, input().split())

g = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

for el in g:
  el.sort()

check = [False] * (n+1)

dfs_ans = []
def dfs(x):
  check[x] = True
  dfs_ans.append(x)

  for y in g[x]:
    if not check[y]:
      dfs(y)

bfs_ans = []
def bfs(x):
  check = [False] * (n+1)
  q = deque()

  check[x] = True
  q.append(x)
  bfs_ans.append(x)

  while q:
    x = q.popleft()
    
    for y in g[x]:
      if not check[y]:
        check[y] = True
        q.append(y)
        bfs_ans.append(y)
  
dfs(v)
print(' '.join(map(str, dfs_ans)))

bfs(v)
print(' '.join(map(str, bfs_ans)))