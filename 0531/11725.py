from collections import deque

class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right


MAX = 100001

parent = [0] * MAX
check = [False] * MAX
depth = [0] * MAX
dist = [0] * MAX

n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n-1):
  u, v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)

depth[1] = 0
check[1] = True

q = deque()
q.append(1)
parent[1] = 0
while q:
  x = q.popleft()
  for y in a[x]:
    if not check[y]:
      depth[y] = depth[x] + 1
      check[y] = True
      parent[y] = x
      q.append(y)

for i in range(2, n+1):
  print(parent[i])