import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  g = [[] for _ in range(n+1)]
  d = [0] * (n+1) # 0: 방문x,  1: 방문 & 그룹 1,  2: 방문 & 그룹2

  for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

  for i in range(1, n+1):
    g[i].sort()


  def dfs(x, c):
    d[x] = c

    for y in g[x]:
      if d[y] == 0:
        dfs(y, 3-c)

  for i in range(1, n+1):
    if d[i] == 0:
      dfs(i, 1)

  ok = True
  for i in range(1, n+1):
    for v in g[i]:
      if d[v] == d[i]:
        ok = False

  print("YES" if ok else "NO")




