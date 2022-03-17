import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = [False] * 10

if m != 0:
  broken_input = list(map(int, input().split()))
  for num in broken_input:
    broken[num] = True  

# 숫자 키로 몇번 눌러서 가능?
def possible(c):
  if c == 0:
    if broken[0] == True:
      return 0
    else:
      return 1

  l = 0
  while c > 0:
    if broken[c % 10]:
      return 0
    l += 1
    c //= 10

  return l

# +, - 만 눌러서 이동 횟수 
answer = abs(n - 100)

for i in range(1000001):
  c = i
  # 숫자키 누르는 횟수 
  l = possible(c)

  if l > 0:
    # 숫자키 다 누르고 +, - 로 이동 횟수 
    press = abs(c-n)
    
    if answer > l + press:
      answer = l + press

print(answer)

