import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
  string = input().split()

  cmd = string[0]
  
  if cmd == 'push':
    s.append(string[1])
  elif cmd == 'pop':
    if not s:
      print(-1)
    else:
      print(s.pop())
  elif cmd == 'size':
    print(len(s))
  elif cmd == 'empty':
    if not s:
      print(1)
    else:
      print(0)
  elif cmd == 'top':
    if not s:
      print(-1)
    else:
      print(s[-1])