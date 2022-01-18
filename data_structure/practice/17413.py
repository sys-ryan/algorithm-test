#단어 뒤집기 2 (태그)

import sys
input = sys.stdin.readline

s = list(input())

is_tag = False
stack = []
ans = []
for el in s:
  if el == '<':
    while stack: 
        ans.append(stack.pop())
    ans.append(el)
    is_tag = True
  elif el == '>':
    ans.append(el)
    is_tag = False
  elif el == ' ' or el == '\n':
    if is_tag:
      ans.append(el)
    else:
      while stack: 
        ans.append(stack.pop())
      ans.append(el)
  else: 
    if is_tag:
      ans.append(el)
    else:
      stack.append(el)
  
for el in ans:
  print(el, end="")


