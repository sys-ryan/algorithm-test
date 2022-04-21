import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  string = input()
  s = []
  ok = True
  for el in string:
    if el == '(':
      s.append(el)
    elif el == ')':
      if not s:
        ok = False
        break
      s.pop()
    
  if ok and not s:
    print("YES")
  else:
    print("NO")