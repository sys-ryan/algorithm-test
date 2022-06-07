from collections import deque
import sys

MAX = 10001
sys.setrecursionlimit(MAX)

def go(n, m):
  if n == m:
    return 
  go(n, via[m])
  print(how[m], end='')

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  check = [False] * MAX
  dist = [-1] * MAX
  via = [-1] * MAX
  how = [''] * MAX

  q = deque()
  
  check[n] = True
  dist[n] = 0 
  via[n] = -1
  q.append(n)

  while q:
    now = q.popleft()
    
    next = (now*2) % 10000
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] = dist[now] + 1
      via[next] = now
      how[next] = 'D'
    
    next = now - 1
    if next == -1:
      next = 9999
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] = dist[now] + 1
      via[next] = now
      how[next] = 'S'
    
    next = (now%1000) * 10 + now // 1000
    if not check[next]:
      q.append(next)
      check[next] = True
      via[next] = now
      how[next] = 'L'
    
    next = (now//10) + (now%10)* 1000
    if not check[next]:
      q.append(next)
      check[next] = True
      via[next] = now
      how[next] = 'R'

  go(n, m)
  print()