string = input()

stack = []
answer = 0
for (index, char) in enumerate(string):
  if char == '(':
    stack.append(index)

  else:
    if stack[-1] + 1 == index: # 레이져 
      stack.pop()
      answer += len(stack)
    else: # 쇠막대 
      stack.pop()
      answer += 1

print(answer)


