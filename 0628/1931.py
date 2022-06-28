from collections import namedtuple

Meeting = namedtuple('Meeting', ['begin', 'end'])

n = int(input())
a = [Meeting(*map(int, input().split())) for _ in range(n)]
a.sort(key=lambda p: (p.end, p.begin))

now = 0
ans = 0
for p in a:
  if now <= p.begin:
    now = p.end
    ans += 1

print(ans)