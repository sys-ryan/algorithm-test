#요세푸스 문제 

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

ans = []
q = deque()

for i in range(n):
  q.append(str(i+1))

while q:
  for i in range(k):
    q.append(q.popleft())
  ans.append(q.pop())

ans_str = ', '.join(ans)
print(f'<{ans_str}>')