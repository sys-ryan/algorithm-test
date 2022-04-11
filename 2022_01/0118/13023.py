import sys

n, m = map(int, input().split())
h = []
g = [[] for _ in range(n)]
x = [[0] * n for _ in range(n)]

for _ in range(m):
  u, v = map(int, input().split())
  h.append((u, v))
  h.append((v, u))

  g[u].append(v)
  g[v].append(u)

  x[u][v] = 1
  x[v][u] = 1

m *= 2 #친구 관계의 수 m 인데, 간선 리스트에 (u, v) (v, u) 양방향으로 2번식 넣음 

for i in range(m):
  for j in range(m):
    #ab, cd
    a, b = h[i]
    c, d = h[j]

    if a == b or a == c or a == d or b == c or b == d or c == d:
      continue
      
    #bc 
    if x[b][c] == 0:
      continue

    #de
    for e in g[d]:
      if a == e or b == e or c == e or d == e:
        continue
      
      print(1)
      sys.exit(0)
    
print(0)