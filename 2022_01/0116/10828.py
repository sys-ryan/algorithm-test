import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
  s = input().split()

  cmd = s[0]

  if cmd == 'push':
    stack.append(s[1])
  elif cmd == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif cmd == 'size':
    print(len(stack))
  elif cmd == 'empty':
    if stack: 
      print(0)
    else:
      print(1)
  elif cmd == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)

  

