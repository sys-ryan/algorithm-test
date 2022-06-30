n = int(input())
a = [int(input()) for _ in range(n)]

stack = []
m = 0 # 마지막으로 스택에 넣은 수 
answer = []
for num in a:

  if m < num:
    while m < num:
      m += 1
      stack.append(m)
      answer.append('+')
    stack.pop()
    answer.append('-')
  else:
    found = False
    if stack:
      if stack[-1] == num:
        stack.pop()
        answer.append('-')
        found = True

    if not found:
      print("NO")
      exit()

for el in answer:
  print(el)