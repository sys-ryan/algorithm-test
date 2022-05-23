n, m = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
def check(password): 
  password = list(password)
  mo = 0
  ja = 0

  for c in password:
    if c in 'aeiou':
      mo += 1
    else:
      ja += 1

  return mo >= 1 and ja >= 2
    

def go(n, alpha, password, i):
  if len(password) == n:
    if check(password):
      print(password)
    return
  
  if i >= len(alpha):
    return
  
  go(n, alpha, password + alpha[i], i+1)
  go(n, alpha, password, i+1)

go(n, alpha, '', 0)

