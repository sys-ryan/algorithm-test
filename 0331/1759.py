def check(password):
  mo = 0
  ja = 0
  for x in password:
    if x in 'aeiou':
      mo += 1
    else:
      ja += 1
    
  return ja >= 2 and mo >= 1


def go(n, alpha, password, i):
  # n: 만들어야 하는 암호의 길이 
  # alpah: 사용할 수 있는 알파벳
  # password: 현재까지 만든 암호 
  # i: 사용할지 말지 결정해야 하는 알파벳의 인덱스

  # 정답을 찾은 경우 : n == len(password)

  # 불가능한 경우 : i >= len(alpha)

  if len(password) == n:
    if check(password):
      print(password)
    return
  
  if i == len(alpha):
    return
  
  go(n, alpha, password+alpha[i], i+1)
  go(n, alpha, password, i+1)

l, c = map(int, input().split())

alpha = list(map(str, input().split()))
alpha.sort()

go(l, alpha, '', 0)