from collections import deque
MAX = 200000

check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)

n, m = map(int, input().split())
check[n] = True
dist[n] = 0

q = deque()
q.append(n)

while q:
  x = q.popleft()

  for y in [x-1, x+1, x*2]:
    if 0 <= y <= MAX and check[y] == False:
      check[y] = True
      dist[y] = dist[x] + 1
      q.append(y)
    
print(dist[m])