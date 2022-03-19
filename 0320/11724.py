import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n ,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  adj[u].append(v)
  adj[v].append(u)

def dfs(x):
  check[x] = True
  for y in adj[x]:
    if not check[y]:
      dfs(y)

components = 0
for i in range(1, n+1):
  if check[i] == False:
    dfs(i)
    components += 1

print(components)