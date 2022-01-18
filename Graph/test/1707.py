import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  g = [[] for _ in range(n+1)]
  color = [0] * (n+1)

  for _ in range(m):
    u, v = map(int ,input().split())
    g[u].append(v)
    g[v].append(u)

  for i in range(1, n+1):
    g[i].sort()

  def dfs(x, c):
    color[x] = c
    for y in g[x]:
      if color[y] == 0:
        dfs(y, 3-c)

  for i in range(1, n+1):
    if color[i] == 0:
      dfs(i, 1)
  
  ok = True
  for i in range(1, n+1):
    for x in g[i]:
      if color[i] == color[x]:
        ok = False

  print("YES" if ok else "NO")


  

  
