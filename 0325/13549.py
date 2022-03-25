from collections import deque

n, k = map(int, input().split())
MAX = 200001

dist = [-1] * MAX

q = deque()
next_q = deque()

q.append(n)
dist[n] = 0

while q:
  x = q.popleft()

  if x*2 < MAX and dist[x*2] == -1:
    dist[x*2] = dist[x]
    q.append(x*2)

  if x+1 < MAX and dist[x+1] == -1:
    dist[x+1] = dist[x] + 1
    next_q.append(x+1)

  if 0 <= x-1 and dist[x-1] == -1:
    dist[x-1] = dist[x] + 1
    next_q.append(x-1)

  if not q:
    q = next_q
    next_q = deque()

print(dist[k])