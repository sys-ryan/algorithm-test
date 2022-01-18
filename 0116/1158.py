import sys
from collections import deque

n, k = map(int, input().split())

q = deque()

for i in range(1, n+1):
  q.append(i)

ans = []

while q:
  for i in range(k):
    q.append(q.popleft())
  ans.append(q.pop())

s = ', '.join(map(str, ans))

print(f'<{s}>')


