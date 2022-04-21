string = list(input())
l = len(string)

s = []
cnt = 0

for i in range(l):
  el = string[i]
  if el == '(':
    s.append(i)
  elif el == ')':
    if s[-1] == i-1:
      s.pop()
      cnt += len(s)
    else:
      s.pop()
      cnt += 1

print(cnt)