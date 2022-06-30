string = list(input()) + [' ']

tag = False
stack = []
answer = []
for char in string:
  if char == '<':
    while stack:
      answer.append(stack.pop())
    tag = True
    answer.append(char)
  elif char == '>':
    tag = False
    answer.append(char)
  elif char == ' ':
    while stack:
      answer.append(stack.pop())
    answer.append(char)
  else:
    if tag:
      answer.append(char)
    else:
      stack.append(char)
answer = ''.join(answer)
print(answer[:-1])
