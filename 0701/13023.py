n, m = map(int, input().split())

a = [[False] *(n+1) for _ in range(n+1)]
g = [[] for _ in range(n+1)]
edges = [] 

for _ in range(m):
  u, v = map(int, input().split())

  edges.append((u, v))
  edges.append((v, u))

  g[u].append(v)
  g[v].append(u)

  a[u][v] = True
  a[v][u] = True


m *= 2

for i in range(m):
  for j in range(m):

    # A -> B
    A, B = edges[i]
    # A = edges[i][0]
    # B = edges[i][1]

    # C -> D
    C, D = edges[j]
    # C = edges[j][0]
    # D = edges[j][1]

    if A == B or A == C or A == D or B == C or B == D or C == D:
      continue

    # B-> C
    if not a[B][C]:
      continue

    for E in g[D]:
      if A == E or B == E or C == E or D == E:
        continue
      print(1)
      exit()

print(0)

    


    
      
    