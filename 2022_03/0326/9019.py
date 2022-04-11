from collections import deque
import sys
sys.setrecursionlimit(10001)

def print_answer(a, b):
  if a == b:
    return
  print_answer(a, from_node[b])
  print(how[b], end='')

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())

  dist = [-1] * 10001
  from_node = [-1] * 10001
  how = [''] * 10001

  q = deque()
  q.append(a)
  dist[a] = 0
  from_node[a] = -1
  how[a] = ''

  while q:
    x = q.popleft()

    next = (x * 2) % 10000
    if dist[next] == -1:
      dist[next] = dist[x] + 1
      from_node[next] = x
      how[next] = 'D'
      q.append(next)
    
    next = x-1
    if next == -1:
      next = 9999
    if dist[next] == -1:
      dist[next] = dist[x] + 1
      from_node[next] = x
      how[next] = 'S'
      q.append(next)

    next = (x % 1000) * 10 + (x // 1000)
    if dist[next] == -1:
      dist[next] = dist[x] + 1
      from_node[next] = x
      how[next] = 'L'
      q.append(next)

    next = (x // 10) + (x % 10) * 1000
    if dist[next] == -1:
      dist[next] = dist[x] + 1
      from_node[next] = x
      how[next] = 'R'
      q.append(next)

  print_answer(a, b)
  print()