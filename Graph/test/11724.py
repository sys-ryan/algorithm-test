import sys

n, m = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

for i in range(1, n+1):
  g[i].sort()


def dfs(x):
  check[x] = True
  for y in g[x]:
    if check[y] == False:
      dfs(y)

c = 0
check = [False] * (n+1)
for i in range(1, n+1):
  if check[i] == False:
    dfs(i)
    c += 1

print(c)