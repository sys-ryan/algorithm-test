from collections import deque

dist = [-1] * 101
next = [0] * 101 

for i in range(1, 101):
  next[i] = i

n, m = map(int, input().split())

for _ in range(n):
  u, v = map(int, input().split())
  next[u] = v

for _ in range(m):
  u, v = map(int, input().split())
  next[u] = v

q = deque()
q.append(1)
dist[1] = 0

while q:
  x = q.popleft()
  
  for i in range(1, 7):
    y = x + i
    if y > 100:
      continue
    y = next[y]
    if dist[y] == -1:
      dist[y] = dist[x] + 1
      q.append(y)

print(dist[100])