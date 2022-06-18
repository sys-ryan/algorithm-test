def calc(a, index, cur, plus, minus, mul, div):
  if index == len(a):
    return [cur]
  
  res = []
  if plus > 0:
    res.extend(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
  if minus > 0:
    res.extend(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
  if mul > 0:
    res.extend(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
  if div > 0:
    if cur >= 0:
      res.extend(calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
    else:
      res.extend(calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
  return res

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
res = calc(a, 1, a[0], plus, minus, mul, div)

print(max(res))
print(min(res))