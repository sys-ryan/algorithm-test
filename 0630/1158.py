from collections import deque 

n, k = map(int, input().split())

q = deque([x+1 for x in range(n)])
answer = []
while q:
  for i in range(1, k+1):
    if i == k:
      answer.append(q.popleft())
    else:
      q.append(q.popleft())
answer = ', '.join(map(str, answer))
print(f'<{answer}>')