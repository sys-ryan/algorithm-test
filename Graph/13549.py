#숨바꼭질 3
import sys
from collections import deque

MAX = 200001

n, k = map(int, input().split())

d = [-1] * MAX
check = [False] * MAX

q = deque()
next_q = deque()

q.append(n)
d[n] = 0
check[n] = True

while q:
  x = q.popleft()

  if x*2 < MAX and check[x*2] == False:
    q.append(x*2)
    d[x*2] = d[x]
    check[x*2] = True
  
  if x+1 < MAX and check[x+1] == False:
    next_q.append(x+1)
    d[x+1] = d[x] + 1
    check[x+1] = True
  
  if x-1 >= 0 and check[x-1] == False:
    next_q.append(x-1)
    d[x-1] = d[x] + 1
    check[x-1] = True

  if not q:
    q = next_q
    next_q = deque()
  
print(d[k])

  
