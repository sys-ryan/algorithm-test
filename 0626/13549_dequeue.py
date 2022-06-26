from collections import deque
MAX = 200000

check = [False] * MAX
dist = [-1] * MAX
n, m = map(int, input().split())

check[n] = True
dist[n] = 0

q = deque()
q.append(n)

while q:
  x = q.popleft()

  if x*2 < MAX and not check[x*2]:
    q.appendleft(x*2)
    dist[x*2] = dist[x]
    check[x*2] = True

  if x-1 >= 0 and not check[x-1]:
    q.append(x-1)
    dist[x-1] = dist[x] + 1
    check[x-1] = True
  
  if x+1 < MAX and not check[x+1]:
    q.append(x+1)
    dist[x+1] = dist[x] + 1
    check[x+1] = True

print(dist[m])

  