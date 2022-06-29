s = input()
num = []
sign = []
minus = False
cur = 0
sign += [1]


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
num += [cur]
ans = 0
minus = False

for i in range(len(num)):
  if sign[i] == -1:
    minus = True
  if minus:
    ans -= num[i]
  else:
    ans += num[i]
print(ans)
