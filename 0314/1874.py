import sys
input = sys.stdin.readline

n = int(input())
stack = []
last_num = 0
ans = ""

for _ in range(n):
  x = int(input())
  if last_num < x:
    while last_num < x:
      last_num += 1
      stack.append(last_num)
      ans += '+'
    stack.pop()
    ans += '-'
  else:
    ok = False
    if stack:
      top = stack[-1]
      stack.pop()
      ans += '-'
      if top == x:
        ok = True
    
    if not ok:
      print("NO")
      exit()

ans_len = len(ans)
for i in range(ans_len):
  print(ans[i])

