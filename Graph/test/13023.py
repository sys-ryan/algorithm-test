import sys

input = sys.stdin.readline
n, m = map(int, input().split())

h = [[False] * (n) for _ in range(n)]
g = [[] for _ in range(n)]
edges = []

for _ in range(m):
  u, v = map(int, input().split())
  edges.append((u, v))
  edges.append((v, u))

  h[u][v] = h[v][u] = 1

  g[u].append(v)
  g[v].append(u)


for i in range(n):
  for j in range(n):
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
      if e == a or e == b or e == c or e == d:
        continue
      print(1)
      sys.exit(0)

print(0)