import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()

for i in range(1, n+1):
  q.append(i)

answer = []

while q:
  for i in range(k):
    q.append(q.popleft())
  answer.append(q.pop())

s = ', '.join(list(map(str, answer)))
answer_str = f'<{s}>'
print(answer_str)