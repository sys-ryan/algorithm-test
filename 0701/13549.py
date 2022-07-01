from collections import deque

n, m = map(int, input().split())

MAX = 200000

dist = [-1] * (MAX+1)

q = deque()
next_q = deque()

q.append(n)
dist[n] = 0

while q:
  now = q.popleft()

  nxt = now*2
  if nxt <= MAX and dist[nxt] == -1:
    q.append(nxt)
    dist[nxt] = dist[now]

  for nxt in [now-1, now+1]:
    if 0 <= nxt <= MAX and dist[nxt] == -1:
      next_q.append(nxt)
      dist[nxt] = dist[now] + 1  

  if not q:
    q = next_q
    next_q = deque()

print(dist[m])