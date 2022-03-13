import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  string = list(input())
  string.pop()
  
  ok = True
  stack = 0
  string_len = len(string)
  for i in range(string_len):
    if string[i] == '(':
      stack += 1
    else:
      stack -= 1
      if stack < 0:
        ok = False
    
  if ok and stack == 0:
    print("YES")
  else:
    print("NO")
