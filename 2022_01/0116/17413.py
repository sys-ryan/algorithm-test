import sys

input = sys.stdin.readline

s = list(input())
slen = len(s)

ans = []
mode = True
for i in range(slen):
  c = s[i]

  if c == '<':
    mode = False
    while ans:
      print(ans.pop(), end='')
    print(c, end='')
  elif c == '>':
    mode = True
    print(c, end='')
  elif c == ' ' or c == '\n':
    while ans:
      print(ans.pop(), end='')
    print(c, end='')
  else: 
    if mode:
      ans.append(c)
    else:
      print(c, end='')

