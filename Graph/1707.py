#이분 그래프
import sys
# sys.setrecursionlimit(1000000)

input = sys.stdin.readline

t = int(input())
  
for _ in range(t):
  n, m = map(int, input().split())

  a = [[] for _ in range(n+1)]
  check = [0] * (n+1)
  color = [0] * (n+1)

  for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

  for i in range(1, n+1):
    a[i].sort()

  def dfs(node, c):
    color[node] = c
    for x in a[node]:
      if color[x] == 0:
        dfs(x, 3-c)

  ok = True
  for i in range(1, n+1):
    if color[i] == 0:
      dfs(i, 1)

  for i in range(1, n+1):
    for x in a[i]:
      if color[i] == color[x]:
        ok = False

  print("YES" if ok else "NO")





  



