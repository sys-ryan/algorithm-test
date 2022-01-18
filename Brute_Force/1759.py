#암호 만들기
import sys



def check(password):
  m = 0
  j = 0
  for c in password:
    if c == 'a' or c == 'e' or c =='i' or c == 'o' or c == 'u':
      m += 1
    else:
      j += 1

  if m >= 1 and j >= 2:
    return True
  else:
    return False

def go(l, alpha, password, i):
  if len(password) == l:
    if check(password):
      print(password)
    return
  
  if i >= len(alpha):
    return
  
  go(l, alpha, password+alpha[i], i+1)
  go(l, alpha, password, i+1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
# password = ''

go(l, alpha, "", 0)



