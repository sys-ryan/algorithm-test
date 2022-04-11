s = input()
num = []
sign = []
minus = False
cur = 0
sign += [1] # 첫 번째 수는 양수

for x in s:
  if x in '+-':
    if x == '+':
      sign += [1]
    else:
      sign += [-1]
  
    num += [cur]
    cur = 0
  else:
    cur = cur * 10 + (ord(x) - ord('0'))

num += [cur] # 마지막 수 처리 



ans = 0
for i in range(len(num)):
  if sign[i] == -1:
    minus = True
  if minus:
    ans -= num[i]
  else:
    ans += num[i]
print(ans)
