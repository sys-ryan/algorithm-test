from collections import deque

n, m = map(int, input().split())
MAX = 200000
dist = [-1] * (MAX+1)
via = [-1] * (MAX+1)


def bfs(n):
  dist[n] = 0
  via[n] = -1
  q = deque()
  q.append(n)

  while q:
    now = q.popleft()

    for nxt in [now-1, now+1, now*2]:
      if 0 <= nxt <= MAX and dist[nxt] == -1:
        dist[nxt] = dist[now] + 1
        via[nxt] = now
        q.append(nxt)

bfs(n)
destination = m
print(dist[m])
stack = []
while destination != n:
  stack.append(destination)
  destination = via[destination]
stack.append(n)
stack.reverse()
print(' '.join(map(str, stack)))
print()
