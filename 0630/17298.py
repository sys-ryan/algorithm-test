n = int(input())
a = list(map(int, input().split()))

stack = []
l = len(a)
answer = [-1] * l
stack.append(0)
for i in range(1, l):
  if not stack:
    stack.append(i)
    continue

  while stack and a[stack[-1]] < a[i]:
    answer[stack[-1]] = a[i]
    stack.pop()
  stack.append(i)

while stack:
  answer[stack[-1]] = -1
  stack.pop()

print(' '.join(map(str, answer)))
