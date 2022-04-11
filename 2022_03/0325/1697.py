from collections import deque

n, k = map(int, input().split())

check = [False] * 100001
dist = [0] * 100001

q = deque()

q.append(n)
check[n] = True
dist[n] = 0

while q:
  x = q.popleft()

  if x-1 >= 0 and not check[x-1]:
    check[x-1] = True
    dist[x-1] = dist[x] + 1
    q.append(x-1)
    
  if x+1 < 100001 and not check[x+1]:
    check[x+1] = True
    dist[x+1] = dist[x] + 1
    q.append(x+1)

  if x*2 < 100001 and not check[x*2]:
    check[x*2] = True
    dist[x*2] = dist[x] + 1
    q.append(x*2)


print(dist[k])