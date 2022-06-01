import sys
input = sys.stdin.readline

s = list(input())
stack = []
ans = ''
tag = False
for el in s:
  
  if el == '<':
    while stack:
      ans += stack.pop()
    tag = True
    ans += el

  elif el == '>':
    tag = False
    ans += el

  elif el == ' ' or el == '\n':
    while stack:
      ans += stack.pop()
    ans += el

  else:
  
    if tag:
      ans += el
    else:
      stack.append(el)

print(ans)