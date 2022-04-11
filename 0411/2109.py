from collections import namedtuple
from heapq import heappush, heappop

Lecture = namedtuple('Lecture', ['p', 'd', 'w'])
n = int(input())
a = []

# lecture 0
for _ in range(n):
  p, d = map(int, input().split())
  a.append(Lecture(p, d, 0))

a.sort(key=lambda x: (x.d, x.p), reverse=True)

q = []
k = 0
ans = 0
for i in range(10000, 0, -1):
  # i일 까지 할 수 있는 강연을 후보에 추가 
  while k < n and a[k].d == i:
    heappush(q, -a[k].p)
    k += 1
  
  # i일에 어떤 강연 할지 선택
  if q:
    ans += -heappop(q)

print(ans)