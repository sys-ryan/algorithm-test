def next_pemutation(a):
  i = len(a) - 1
  while i > 0 and a[i-1] >= a[i]:
    i -= 1

  if i <= 0:
    return False

  j = len(a) - 1
  while a[j] <= a[i-1]:
    j -= 1

  a[i-1], a[j] = a[j], a[i-1]

  j = len(a) - 1
  while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

  return True


def div(a, b):
  if a >= 0:
    return a//b
  else:
    return -(a//b)

def calc(a, op):
  n = len(a)
  ans = a[0]
  for i in range(1, n):
    if op[i-1] == 0:
      ans = ans + a[i]
    elif op[i-1] == 1:
      ans = ans - a[i]
    elif op[i-1] == 2:
      ans = ans * a[i]
    else:
      ans = div(ans, a[i])

  return ans


n = int(input())
a = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
op = []

for i, cnt in enumerate(op_cnt):
  for k in range(cnt):
    op.append(i)

op.sort()
ans = []

while True:
  temp = calc(a, op)
  ans.append(temp)
  if not next_pemutation(op):
    break

ans.sort()
print(ans[-1])
print(ans[0])