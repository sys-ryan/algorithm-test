#에디터 

import sys

input = sys.stdin.readline

left = list(input())
left.pop()
right = []

n = int(input())

for _ in range(n):
  s = input().split()
  cmd = s[0]

  if cmd == "L":
    if left: 
      right.append(left.pop())
  elif cmd == "D":
    if right:
      left.append(right.pop())
  elif cmd == "B":
    if left: 
      left.pop()
  elif cmd == "P":
    left.append(s[1])
  

for el in left:
  print(el, end="")

r_idx = len(right)
for i in range(r_idx, 0, -1):
  print(right[i-1], end="")

print("\n")