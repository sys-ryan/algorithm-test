import sys
from collections import deque

n = int(input())

MAX = 2001
d = [[-1] * MAX for _ in range(MAX)]

d[1][0] = 0
q = deque()
q.append((1, 0))

while q:
  s, c = q.popleft()

  # (s, c) -> (s, s)
  if d[s][s] == -1:
    d[s][s] = d[s][c] + 1
    q.append((s, s))

  # (s ,c) -> (s+c, c)
  if s+c <= n and d[s+c][c] == -1:
    d[s+c][c] = d[s][c] + 1
    q.append((s+c, c))

  # (s, c) -> (s-1, c)
  if s-1 >= 0 and d[s-1][c] == -1:
    d[s-1][c] = d[s][c] + 1
    q.append((s-1, c))
ans = -1
for i in range(0, n+1):
  if d[n][i] != -1:
    if ans == -1 or ans > d[n][i]:
      ans = d[n][i]

print(ans)