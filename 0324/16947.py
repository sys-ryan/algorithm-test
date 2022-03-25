import sys
from collections import deque 

sys.setrecursionlimit(10**6)

n = int(input())

dist = [-1] * (n+1)
check = [0] * (n+1) # 0 : not visited, 1: visited, 2: cycle
adj_list = [[] for _ in range(n+1)]

for i in range(1, n+1):
  u, v = map(int, input().split())
  adj_list[u].append(v)
  adj_list[v].append(u)

for i in range(1, n+1):
  adj_list[i].sort()

# p -> x
def find_cycle(x, p):
  # -2 : found cycle and not included
  # -1 : not a cycle
  # n : found cycle and start index (>=0)

  if check[x] == 1:
    # cycle
    return x
  
  check[x] = 1
  for y in adj_list[x]:
    if y == p:
      # previous node
      continue 

    res = find_cycle(y, x)

    if res == -2:
      return -2
    if res >= 0:
      check[x] = 2
      if x == res:
        return -2
      else:
        return res
  return -1

def calc_dist():
  q = deque()

  for i in range(1, n+1):
    if check[i] == 2:
      q.append(i)
      dist[i] = 0
    else:
      dist[i] = -1

  while q:
    x = q.popleft()
    for y in adj_list[x]:
      if dist[y] == -1:
        dist[y] = dist[x] + 1
        q.append(y)
  
  for i in range(1, n+1):
    print(dist[i], end=' ')
  print()

find_cycle(1, 0)
calc_dist()