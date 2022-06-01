import sys
input = sys.stdin.readline

left = list(input())
left.pop()
right = []

n = int(input())

for _ in range(n):
  string = input().split()

  if string[0] == 'L':
    if left:
      right.append(left.pop())

  elif string[0] == 'D':
    if right:
      left.append(right.pop())

  elif string[0] == 'B':
    if left:
      left.pop()

  elif string[0] == 'P':
    left.append(string[1])

length = len(right)
for _ in range(length):
  left.append(right.pop())

print(''.join(left))





