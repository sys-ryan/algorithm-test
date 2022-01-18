#DFS와 BFS - 인접 리스트
import sys
from collections import deque

n, m, start = map(int, input().split())

a = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)


for i in range(1, n+1):
  a[i].sort()

def dfs(x):
  check[x] = True
  # print("x: " + str(x))
  print(x, end= ' ')
  for y in a[x]:
    if check[y] ==False:
      dfs(y)

def bfs(start):
  
  check = [False] * (n+1)
  q = deque()
  q.append(start)
  check[start] = True
  while q:
    x = q.popleft()
    print(x, end=" ")
    for y in a[x]:
      if check[y] == False:
        check[y] = True
        q.append(y)

# print("v : " + str(v))
dfs(start)
print()
bfs(start)
print()