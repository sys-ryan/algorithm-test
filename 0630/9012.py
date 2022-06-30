t = int(input())

for _ in range(t):
  stack = 0

  string = input()
  ok = True
  for char in string:
    if char == '(':
      stack += 1
    else:
      stack -= 1
      
      if stack < 0:
        print("NO")
        ok = False
        break
  
  if stack > 0:
    print("NO")
    ok = False
  
  if ok:
    print("YES")
