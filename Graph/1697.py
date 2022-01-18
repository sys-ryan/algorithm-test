#숨바꼭질
import sys
from collections import deque

MAX = 2000001

d = [-1] * MAX
check = [False] * MAX

q = deque()

n, k = map(int, input().split())

q.append(n)
d[n]= 0
check[n] = True

while q:
  x = q.popleft()
  
  if x - 1 >= 0:
    if check[x-1] == False:
      check[x-1] = True
      d[x-1] = d[x] + 1
      q.append(x-1)
  
  if x + 1 < MAX:
    if check[x+1] == False:
      check[x+1] = True
      d[x+1] = d[x] + 1
      q.append(x+1)
  
  if x*2 < MAX:
    if check[x*2] == False:
      check[x*2] = True
      d[x*2] = d[x]+1
      q.append(x*2)

print(d[k])
