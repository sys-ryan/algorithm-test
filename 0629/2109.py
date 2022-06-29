from collections import namedtuple
from collections import deque
from heapq import heappush, heappop

Lecture = namedtuple('Lecture', ['p', 'd'])

n = int(input())
lectures = []

for i in range(n):
  p, d = map(int, input().split())
  lectures.append(Lecture(-p, d))

lectures.sort(key=lambda x: (x.d, x.p), reverse=True)
# print(lectures)
k = 0
ans = 0
q = []
for i in range(10000, 0, -1):
  while k < n and lectures[k].d == i:
    heappush(q, lectures[k].p)
    k += 1
  if q:
    # print(i, q)
    # print(q.pop())
    ans += heappop(q)
  # print(f'ans: {ans}')

print(-ans)
