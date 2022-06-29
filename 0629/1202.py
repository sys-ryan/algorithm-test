import sys
from collections import namedtuple
from heapq import heappush, heappop
input = sys.stdin.readline

Jewel = namedtuple('Jewel', ['m', 'v', 'w']) # m: 무게, v: 가격, w: 0 - 보석 / 1 - 가방

n, k = map(int, input().split())
a = []

for _ in range(n):
  m, v = map(int, input().split())
  a.append(Jewel(m, v, 0))

for _ in range(k):
  m = int(input())
  a.append(Jewel(m, 0, 1))

a.sort(key=lambda p: (p.m, p.w))
q = []
ans = 0

for p in a:
  if p.w == 0: #보석
    heappush(q, -p.v)
  else:
    if q: # 가방이 나올 때마다 힙에서 가장 비싼 보석을 넣음
      ans += -heappop(q)
print(ans)
