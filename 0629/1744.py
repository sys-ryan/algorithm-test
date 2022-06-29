n = int(input())
plus = []
minus = []
zero = 0
one = 0

for _ in range(n):
  x = int(input())
  if x == 1:
    one += 1
  elif x > 0:
    plus += [x]
  elif x < 0:
    minus += [x]
  else:
    zero += 1

plus.sort()
minus.sort()
plus.reverse()

if len(plus) % 2 == 1: # 양수 두 개씩 묶기 위해, 홀수 개일 경우 1 추가 
  plus += [1]

if len(minus) % 2 == 1:
  minus += [0 if zero > 0 else 1] # 0이 있을 경우, 음수가 홀수개 일 때 0과 묶어서 하나 없애줌 

ans = one
for i in range(0, len(plus), 2):
  ans += plus[i] * plus[i+1]
for i in range(0, len(minus), 2):
  ans += minus[i] * minus[i+1]
print(ans)