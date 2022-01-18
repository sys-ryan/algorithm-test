#단어 뒤집기 

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  stack = []
  s = input()

  s_len = len(s)
  for i in range(s_len):
    if s[i] == ' ' or s[i] == '\n':
      while stack:
        print(stack.pop(), end="")
      print(s[i], end="")
    else:
      stack.append(s[i])


