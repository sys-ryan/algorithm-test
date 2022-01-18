#ABCDE

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
h = [[False] * n for _ in range(n)]
g = [[] for _ in range(n)]


for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))

    h[u][v] = h[v][u] = True

    g[u].append(v)
    g[v].append(u)


m *= 2

for i in range(m):
  for j in range(m):
    #ab, cd
    a, b = edges[i]
    c, d = edges[j]
    if a == b or a == c or a == d or b == c or b == d or c == d:
      continue

    #bc
    if not h[b][c]:
      continue

    #de 
    for e in g[d]:
      if a == e or b == e or c == e or d == e:
        continue
      print(1)
      sys.exit(0)
print(0)
