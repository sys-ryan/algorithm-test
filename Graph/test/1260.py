import sys
from collections import deque

n, m, start = map(int, input().split())

# g = [[] for _ in range(n+1)]

g = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  # g[u].append(v)
  # g[v].append(u)
  g[u][v] = g[v][u] = 1

# for i in range(1, n+1):
#   g[i].sort()

check = [False] * (n+1)
def dfs(x):
  global check
  check[x] = True
  print(x, end=' ')
  # for y in g[x]:
  #   if check[y] == False:
  #     dfs(y)
  for i in range(1,n+1):
    
    if g[x][i] == 1 and check[i] == False:
      dfs(i)
      

def bfs(start):
  check = [False] * (n+1)
  q = deque()
  
  check[start] = True
  q.append(start)

  while q:
    x = q.popleft()
    print(x, end=' ')
    # for y in g[x]:
    #   if check[y] == False:
    #     check[y] = True
    #     q.append(y)
    for i in range(1, n+1):
      if g[x][i] == 1 and check[i] == False:
        check[i] = True
        q.append(i)

dfs(start)
print()
bfs(start)
print()


