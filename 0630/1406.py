import sys
input = sys.stdin.readline

left_stack = list(input())
right_stack = []
n = int(input())
for _ in range(n):
  cmd = input()[:-1].split(' ')
  # cmd = input().split(' ')

  if cmd[0] == 'L':
    if left_stack:
      right_stack.append(left_stack.pop())
  elif cmd[0] == 'D':
    if right_stack:
      left_stack.append(right_stack.pop())
  elif cmd[0] == 'B':
    if left_stack:
      left_stack.pop()
  elif cmd[0] == 'P':
    left_stack.append(str(cmd[1]))
right_stack.reverse()
answer = ''.join(left_stack)  + ''.join(right_stack)
# print(left_stack)
# print(right_stack)
print(answer)