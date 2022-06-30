l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()

def check(password):
  mo = 0
  ja = 0

  for char in password:
    if char in 'aeiou':
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

  go(n, alpha, password+alpha[i], i+1)
  go(n ,alpha, password, i+1)

go(l, alpha, '', 0)