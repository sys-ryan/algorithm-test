import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  s = 0
  good = True

  string = input()

  slen = len(string)

  for i in range(slen):
    c = string[i]

    if c == '(':
      s += 1
    elif c == ')':
      s -= 1
    
    if s < 0:
      good = False

  if s > 0:
    good = False

  print("YES" if good else "NO")

     

     
