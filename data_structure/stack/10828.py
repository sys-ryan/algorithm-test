#스택 

import sys

input = sys.stdin.readline

n = int(input())

top = 0
stack = []

for _ in range(n):
  s = input().split()
  cmd = s[0]

  if cmd == "push":
    stack.append(int(s[1]))
    top += 1
  elif cmd == "pop":
    if stack:
      print(stack.pop())
      top -= 1
    else:
      print(-1)
  elif cmd == "size":
    print(top)
  elif cmd == "empty":
    if not stack: 
      print(1)
    else:
      print(0)
  elif cmd == "top":
    if stack:
      print(stack[top-1])
    else:
      print(-1)


