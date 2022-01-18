#괄호 짝, 괄호 검ㅏ

import sys

input = sys.stdin.readline

n = int(input())

def isValid(s):
  s_len = len(s) - 1
  cnt = 0
  for i in range(s_len):
    if s[i] == "(":
      cnt += 1
    else: 
      cnt -= 1
    
    if cnt < 0:
      print("NO")
      return
  
  if cnt == 0:
    print("YES")
  else:
    print("NO")
  

for _ in range(n):
  s = list(input())
  isValid(s)



  

  