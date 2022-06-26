from collections import deque

MAX = 200000

check = [False] * MAX
dist = [-1] * MAX
n, m = map(int, input().split())

check[n] = True
dist[n] = 0
q = deque()
next_q = deque()
q.append(n)

while q:
  x = q.popleft()
  if x*2 < MAX and check[x*2] == False:
    q.append(x*2)
    check[x*2] = True
    dist[x*2] = dist[x]
  if x-1 >= 0 and check[x-1] == False:
    next_q.append(x-1)
    check[x-1] = True
    dist[x-1] = dist[x] + 1
  if x+1 < MAX and check[x+1] == False:
    next_q.append(x+1)
    check[x+1] = True
    dist[x+1] = dist[x] + 1
  if not q:
    q = next_q
    next_q = deque()
  
print(dist[m])