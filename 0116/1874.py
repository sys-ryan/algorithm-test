import sys
input = sys.stdin.readline

n = int(input())
check = [False] * (n+1)
s = 0
stack = [0]
ans = []

for _ in range(n):
  m = int(input())
  
  if s < m:
    while s != m:
      s += 1
      stack.append(s)
      ans.append('+')
    stack.pop()
    ans.append('-')

  elif stack[-1] == m:
    stack.pop()
    ans.append('-')

  elif stack[-1] > m:
    print("NO")
    sys.exit(0)

for el in ans:
  print(el)
