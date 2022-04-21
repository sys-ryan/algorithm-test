import sys
input = sys.stdin.readline

left = list(input())
left.pop()
m = int(input())

right = []

for i in range(m):
  c = input().split()
  cmd = c[0]

  if cmd == 'L':
    if left:
      right.append(left.pop())
  elif cmd == 'D':
    if right:
      left.append(right.pop())
  elif cmd == 'B':
    if left:
      left.pop()
  elif cmd == 'P':
    left.append(c[1])

while right:
  left.append(right.pop())

print(''.join(map(str, left)))