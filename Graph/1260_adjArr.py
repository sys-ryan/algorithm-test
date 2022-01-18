#DFS와 BFS - 인접 행렬
import sys
from collections import deque

n, m, start = map(int, input().split())

a = [[False] * (n+1) for _ in range(n+1)]

check = [False] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  a[u][v] = a[v][u] = True


def dfs(x):
  check[x] = True
  print(x, end=' ')
  for i in range(1, n+1):
    if a[x][i] and check[i] == False:
      dfs(i)

def bfs(start):
  check = [False] * (n+1)
  q = deque()

  check[start] = True
  q.append(start)

  while q:
    x = q.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
      if a[x][i] and check[i] == False:
        check[i] = True
        q.append(i)


dfs(start)
print()
bfs(start)
print()
