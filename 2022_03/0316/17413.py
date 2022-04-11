import sys
input = sys.stdin.readline

s = list(input())
s_len = len(s)

is_reverse = True
stack = []
# answer = []
for i in range(s_len):
  
  if s[i] == '<':
    is_reverse = False
    while stack:
      print(stack.pop(), end='')
    print(s[i], end='')

  elif s[i] == '>':
    is_reverse = True
    print(s[i], end='')

  elif s[i] == ' ':
    if is_reverse:
      while stack:
        print(stack.pop(), end='')
      print(' ', end='')
    else:
      print(s[i], end='')

  elif s[i] == '\n':
    if is_reverse:
      while stack:
        print(stack.pop(), end='')
        
  else:
    if is_reverse:
      stack.append(s[i])
    else:
      print(s[i], end='')

print()
