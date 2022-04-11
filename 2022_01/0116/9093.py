import sys
input = sys.stdin.readline
s = []

n = int(input())


for _ in range(n):
  string = input()

  l = len(string)
  for i in range(l):
    c = string[i]
    
    if c == ' ' or c == '\n':
      while s:  
        print(s.pop(), end='')
      print(c, end='')
    else:
      s.append(c)

