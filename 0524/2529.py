n = int(input())
operators = list(input().split())
ans = []
check = [False] * 10

def good(num, i, op):
  num = int(num)
  if op == '<':
    return num < i
  elif op == '>':
    return num > i

def go(index, num):
  if index == n+1:
    ans.append(num)
    return

  for i in range(10):
    if check[i]:
      continue
    if index == 0 or good(num[index-1], i, operators[index-1]):
      check[i] = True
      go(index+1, num + str(i))
      check[i] = False

go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])