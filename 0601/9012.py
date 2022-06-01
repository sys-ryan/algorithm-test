n = int(input())

for _ in range(n):
  string = list(input())
  
  stack =[]
  ok = True
  for el in string:
    if el == '(':
      stack.append(el)
    else:
      if not stack:
        ok = False
        break

      stack.pop()

  if stack:
    ok = False
      
  print("YES" if ok else "NO")