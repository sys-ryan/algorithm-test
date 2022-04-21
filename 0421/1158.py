from collections import deque
q = deque()

n, m = map(int, input().split())
ans = []
for i in range(1, n+1):
  q.append(i)

for i in range(n-1):
  for j in range(m-1):
    q.append(q.popleft())
  ans += [q.popleft()]

ans += [q[0]]
ans_str = ', '.join(map(str, ans))
print(f'<{ans_str}>')