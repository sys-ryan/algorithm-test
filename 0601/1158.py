from collections import deque

n, m = map(int, input().split())

q = deque()

for i in range(1, n+1):
  q.append(i)

ans = []
while q:
  for k in range(m):
    q.append(q.popleft())
  ans.append(q.pop())

ans = ', '.join(map(str, ans))
print(f'<{ans}>')