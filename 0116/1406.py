import sys

left = list(input())
right = [] 

# s = input()
n = int(input())

for _ in range(n):
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

# print(left)
# print(right)
while left:
  right.append(left.pop())

while right:
  print(right.pop(), end='')
print()