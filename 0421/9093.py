import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  s = []
  string = input()
  
  for i in string:  
    if i == ' ' or i == '\n':
      while s:
        print(s.pop(), end='')
      print(i, end='')
    else:
      s.append(i)