from collections import deque 

MAX = 200001

n, m = map(int, input().split())

check = [False] * 200001
dist = [0] * 200001

q = deque()

q.append(n)
check[n] = True
dist[n] = 0

while q:
  x  = q.popleft()

  if x-1 >= 0 and not check[x-1]:
    q.append(x-1)
    check[x-1] = True
    dist[x-1] = dist[x] + 1
  
  if x+1 < MAX and not check[x+1]:
    q.append(x+1)
    check[x+1] = True
    dist[x+1] = dist[x] + 1

  if x*2 < MAX and not check[x*2]:
    q.append(2*x)
    check[2*x] = True
    dist[2*x] = dist[x] + 1


print(dist[m])
