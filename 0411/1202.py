from collections import namedtuple
from heapq import heappush, heappop

Jewel = namedtuple('Jewel', ['m', 'v', 'w'])

n, k = map(int, input().split())
a = []

# 보석 0
for _ in range(n):
  m, v = map(int, input().split())
  a.append(Jewel(m, v, 0))

# 가방 1
for _ in range(k):
  m = int(input())
  a.append(Jewel(m, 0, 1))

a.sort(key=lambda p: (p.m, p.w))

q = []
ans = 0
for p in a:
  if p.w == 0:
    heappush(q, -p.v)
  else:
    if q:
      ans += -heappop(q)

print(ans)