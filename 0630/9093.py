stack = [] 

t = int(input())

for _ in range(t):
  string = list(input()) + [' ']
  
  answer = ''
  for char in string:
    if char != ' ':
      stack.append(char)
    elif char == ' ':
      while stack:
        answer += stack.pop()
      answer += char

  print(answer)
