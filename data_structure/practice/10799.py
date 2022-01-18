#쇠막대기 

import sys
input = sys.stdin.readline

s = list(input())
s_len = len(s)

stack = []
cnt = 0

for i in range(s_len):
  el = s[i]
  if el == '(':
    stack.append(i)
  elif el == ')':
    if stack[-1] == i-1:
      stack.pop()
      cnt += len(stack)
    else: 
      stack.pop()
      cnt += 1

print(cnt)