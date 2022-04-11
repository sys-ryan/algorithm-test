import sys
from collections import deque

input = sys.stdin.readline

n, m ,start = map(int, input().split())

a = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  a[u][v] = a[v][u] = 1

d = [-1] * (n+1)

def dfs(x):
  d[x] = 1
  print(x, end=' ')

  for i in range(1, n+1):
    if a[x][i] == 1 and d[i] == -1:
      dfs(i)

def bfs(start):
  d = [-1] * (n+1)
  q = deque()

  q.append(start)
  d[start] = 1

  while q:
    x = q.popleft()
    print(x, end=' ')
    
    for i in range(1, n+1):
      if a[x][i] == 1 and d[i] == -1:
        q.append(i)
        d[i] = 1
  

dfs(start)
print()
  
bfs(start)
print()