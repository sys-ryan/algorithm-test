import sys
s = list(input())

stack = []
length = len(s)
ans = 0
for i in range(length):
  if s[i] == '(':
    stack.append(i)
  else:
    if stack[-1] + 1 == i:
      stack.pop()
      ans += len(stack)
      
    else:
      stack.pop()
      ans += 1
      

print(ans)