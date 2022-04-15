from collections import namedtuple

User = namedtuple('User', ['age', 'name', 'join'])

n = int(input())
a = []
for i in range(n):
  string = input().split(' ')
  age = int(string[0])
  name = string[1]

  a.append(User(age=age, name=name, join=i))

a.sort(key=lambda p: (p.age, p.join))

for el in a:
  print(f'{el.age} {el.name}')