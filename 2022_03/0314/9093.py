import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
  string = input()
  
  stack = []
  string_len = len(string) 
  for i in range(string_len):
    if string[i] == ' ':
      while stack:
        print(stack.pop(), end="")
      print(' ', end='')
    elif string[i] == '\n':
      while stack:
        print(stack.pop(), end="")
      print('\n', end='')
    else:
      stack.append(string[i])