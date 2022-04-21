string = list(input())

s = []
ans = []

tag = False
for ch in string:
  if ch == '<':
    while s:
      print(s.pop(), end='')
    tag = True
    print(ch, end='')
  elif ch == '>':
    tag = False
    print(ch, end='')
  elif ch == ' ':
    while s:
      print(s.pop(), end='')
    print(ch, end='')
  else:
    if tag:
      print(ch, end='')
    else:
      s.append(ch)

while s:
  print(s.pop(), end='')
print()



    