from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
n = int(input())
a = [Point(*map(int, input().split())) for _ in range(n)]

a.sort(key=lambda p: (p.x, p.y))

for el in a:
  print(f'{el.x} {el.y}')