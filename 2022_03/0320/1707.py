import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, color):
  check[x] = color
  for y in adj[x]:
    if not check[y]:
      dfs(y, 3-color)

k = int(input())
for _ in range(k):
  v, e = map(int, input().split())

  adj = [[] for _ in range(v+1)]
  check = [0] * (v+1)

  for i in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

  for i in range(1, v+1):
    if check[i] == 0:
      dfs(i, 1)
  
  ok = True
  for i in range(1, v+1):
    for j in adj[i]:
      if check[i] == check[j]:
        ok = False

  if ok:
    print("YES")
  else:
    print("NO")

    

  