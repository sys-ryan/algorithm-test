n = int(input())
a = [int(input()) for _ in range(n)]

plus = []
minus = []
zero = 0
one = 0

for i in range(n):
  x = a[i]
  if x == 1:
    one += 1
  elif x > 0:
    plus += [x]
  elif x < 0:
    minus += [x]
  elif x == 0:
    zero += 1

plus.sort()
plus.reverse()
minus.sort()

if len(plus) % 2 == 1:
  plus += [1] # since 1*x = x
if len(minus) % 2 == 1:
  minus += [0 if zero > 0 else 1] # since 0*x = 0.. 0이 하나라도 있으면 0 곱해서 제거 

ans = one # 1은 곱하지 않는 것이 최댓값 만든느데 유리 
for i in range(0, len(plus), 2):
  ans += plus[i] * plus[i+1]
for i in range(0, len(minus), 2):
  ans += minus[i] * minus[i+1]
print(ans)