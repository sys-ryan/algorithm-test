import sys

n = int(input())
ops = input().split()

# print(ops)
check = [False] * 10
ans = []
def good(n, i, op):
  n = int(n)
  if op == '<':
    return n < i
  else:
    return n > i


def go(index, num):
  if index == n+1:
    # print(num)
    ans.append(num)
    return
  
  for i in range(0, 10):
    if check[i] == False:
      if index == 0 or good(num[index-1], i, ops[index-1]):
        check[i] = True
        go(index+1, num+str(i))
        check[i] = False


go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])
