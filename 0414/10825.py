from collections import namedtuple
from unicodedata import name
Student = namedtuple('Student', ['name', 'korean', 'english', 'math'])

n = int(input())
a = []

for _ in range(n):
  string = input().split(' ')
  a.append(Student(name=string[0], korean=int(string[1]), english=int(string[2]), math=int(string[3])))

a.sort(key=lambda x: (-x.korean, x.english, -x.math, x.name))

for el in a:
  print(el.name)