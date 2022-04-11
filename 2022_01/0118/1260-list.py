import sys
from collections import deque

input = sys.stdin.readline

n, m, start = map(int,input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

#방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
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
        q.append(y)
        check[y] = True


dfs(start)
print()

bfs(start)
print()