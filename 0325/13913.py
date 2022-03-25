from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

MAX = 100001

check = [False] * MAX
dist =  [0] * MAX
from_node = [-1] * MAX

q = deque()

q.append(n)
check[n] = True
dist[n] = 0

while q:
  x = q.popleft()
  
  if 0 <= x-1 and not check[x-1]:
    check[x-1] = True
    dist[x-1] = dist[x] + 1
    from_node[x-1] = x
    q.append(x-1)

  if x+1 < MAX and not check[x+1]:
    check[x+1] = True
    dist[x+1] = dist[x] + 1
    from_node[x+1] = x
    q.append(x+1)

  if x*2 < MAX and not check[x*2]:
    check[x*2] = True
    dist[x*2] = dist[x] + 1
    from_node[x*2] = x
    q.append(x*2)

print(dist[k])

def print_trace(n, m): #n -> m
  if n != m:
    print_trace(n, from_node[m])
  print(m, end=' ')

def print_trace2(n, m):
  stack = deque()
  i = m
  while i != n:
    stack.append(i)
    i = from_node[i]
  stack.append(n)
  while stack:
    print(stack.pop(), end=' ')
  print()


# print_trace(n, k)

print_trace2(n, k)
  
# print()

