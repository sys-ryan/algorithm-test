import sys
from collections import namedtuple

Meeting = namedtuple('Meeting', ['begin', 'end'])

n = int(input())
a = [Meeting(*map(int, input().split())) for _ in range(n)]
a.sort(key=lambda p: (p.end, p.begin))

now = 0 # 회의가 끝난 시간
ans = 0
for p in a:
  if now <= p.begin: #회의가 끝난 시간이 다음 회의의 begin 보다 더 빠르면, 
    now = p.end
    ans += 1

print(ans)