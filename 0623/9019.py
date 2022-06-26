from collections import deque

t = int(input())
MAX = 10001

for _ in range(t):
  n, m = map(int, input().split())
  check = [False] * MAX
  dist = [-1] * MAX
  via = [-1] * MAX
  how = [''] * MAX
  
  check[n] = True
  dist[n] = 0
  via[n] = -1

  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    # D
    next = (x*2) % 10000
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] = dist[x] + 1
      via[next] = x
      how[next] = 'D'
    
    # S
    next = x-1
    if next == -1:
      next = 9999
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] = dist[x] + 1
      via[next] = x
      how[next] = 'S'
    
    # L
    next = (x%1000) * 10 + x//1000
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] = dist[x] + 1
      via[next] = x
      how[next] = 'L'
    
    next = (x//10) + (x%10)*1000
    if not check[next]:
      q.append(next)
      check[next] = True
      dist[next] =dist[x] + 1
      via[next] = x
      how[next] = 'R'

  res = []

  while how[m] != how[n]:
    res.append(how[m])
    m = via[m]

  res.reverse()
  
  print(''.join(map(str, res)))


