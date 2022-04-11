n, m = map(int, input().split())

h = []
g = [[] for _ in range(n)]
x = [[0] * n for _ in range(n)]

for _ in range(m):
  u, v = map(int, input().split())
  h.append((u, v))
  h.append((v, u))

  g[v].append(u)
  g[u].append(v)

  x[u][v] = x[v][u] = 1

m *= 2

for i in range(m):
  for j in range(m):
    # ab, cd
    a, b = h[i]
    c, d = h[j]

    if a == b or a == c or a == d or b == c or b == d or c == d:
      continue

    # bc
    if x[b][c] == 0:
      continue

    # de
    for e in g[d]:
      if a == e or b == e or c == e or d == e:
        continue
    
      print(1)
      exit()
  
print(0)