import sys
input = sys.stdin.readline

left = list(input())
left.pop()

right = []

m = int(input())
for _ in range(m):
  cmd = input().split()

  if cmd[0] == 'L':
    if left:
      right.append(left.pop())
  
  elif cmd[0] == 'D':
    if right:
      left.append(right.pop())
  
  elif cmd[0] == 'B':
    if left:
      left.pop()

  elif cmd[0] == 'P':
    left.append(cmd[1])

while left:
  right.append(left.pop())

while right:
  print(right.pop(), end='')
print()
