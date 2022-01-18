import sys

s = list(input())
stack = []
ans = 0
i = 0
for el in s:
  if el == '(':
    stack.append(i)
  elif el == ')':
    if stack[-1] + 1 == i:
      stack.pop()
      ans += len(stack)
    else:
      ans += 1
      stack.pop()
  i+=1

print(ans)
