import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
k = int(input())


def dfs(x, c):
  color[x] = c

  for y in g[x]:
    if color[y] == 0:
      dfs(y, 3-c)

for _ in range(k):
  color = [0] * 20001
  v, e = map(int, input().split())

  g = [[] for _ in range(v+1)]

  for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a) 

  
  for i in range(1, v+1):
    if color[i] == 0:
      dfs(i, 1)

  ok = True
  for i in range(1, v+1):
    for j in g[i]:
      if color[i] == color[j]:
        ok = False

  if ok:
    print("YES")
  else:
    print("NO")