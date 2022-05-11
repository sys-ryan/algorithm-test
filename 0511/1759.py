def check(password):
  consonant = 0
  vowel = 0

  for c in password:     
    if c in 'aeiou':
      vowel += 1
    else:
      consonant += 1

  return vowel >= 1 and consonant >= 2

def go(n, alpha, password, i):
  # 비밀번호 길이 n 
  # 사용 가능한 알파벳 []
  # 현재까지 만든 비밀번호
  # i 번째 인덱스 포함/미포함 선택 

  if len(password) == n:
    if check(password):
      print(password)
    return
    # 결과 프린트 

  if len(alpha) == i:
    return 
  
  go(n ,alpha, password + alpha[i], i+1)
  go(n, alpha, password, i+1)

n, l = map(int, input().split())
alpha = list(map(str, input().split()))

alpha.sort()

go(n, alpha, '', 0)