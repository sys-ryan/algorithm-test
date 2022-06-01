n = int(input())

for _ in range(n):
  stack = []

  string = input()
  string += '\n'
  
  for el in string:
    if el == ' ' or el == '\n':
      while stack:
        print(stack.pop(), end='')
      print(el, end='')
    else:
      stack.append(el)
