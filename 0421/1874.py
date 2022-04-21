import sys
input = sys.stdin.readline

n = int(input())

m = 0
s = []
ans = []
for _ in range(n):
  x = int(input())
  if x > m:
    while x > m:
      m += 1
      s.append(m)
      ans.append('+')
    s.pop()
    ans.append('-')
  else:
    found = False
    if s:
      top = s.pop()
      ans.append('-')
      if x == top:
        found = True
  
    if not found:
      print("NO")
      exit()

for el in ans:
  print(el)