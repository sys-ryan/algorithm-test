## 시간초과
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

operators = []
for i in range(plus):
  operators.append('+')
for i in range(minus):
  operators.append('-')
for i in range(mul):
  operators.append('*')
for i in range(div):
  operators.append('/')


def calc(n1, n2, op):
  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    if n1 >= 0:
      return n1 // n2
    else:
      return -(-n1 // n2)

operators = list(permutations(operators, n-1))

res = []
for ops in operators:
  idx = 0
  cur = a[idx]
  idx += 1
  for op in ops:
    n = a[idx]
    cur = calc(cur, n, op)
    idx += 1
  res.append(cur)

print(max(res))
print(min(res))


