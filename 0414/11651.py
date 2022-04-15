from collections import namedtuple
from unicodedata import name
Point = namedtuple('Point', ['x', 'y'])

n = int(input())
a = [Point(*map(int, input().split())) for _ in range(n)]

a.sort(key=lambda p: (p.y, p.x))

for el in a:
  print(f'{el.x} {el.y}')
