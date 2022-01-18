#스택 수열

import sys

input = sys.stdin.readline

n = int(input())

stack = []
ans = []
m = 0

for _ in range(n):
  num = int(input())

  if m < num:
    while m != num:
      m += 1 
      stack.append(m)
      ans.append('+')
    stack.pop()
    ans.append('-')
  else: 
    if stack[-1] != num: 
      print("NO")
      sys.exit(0)
    
    stack.pop()
    ans.append('-')


for el in ans:
  print(el)
    
  
