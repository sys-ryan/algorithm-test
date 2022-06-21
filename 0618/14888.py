def calc(a, index, cur, plus, minus, mul, div):
  # a: 입력으로 주어진 수열
  # index: 현재 계산해야 하는 인덱스 
  # cur: index-1 번째까지 계산한 결과
  # plus, minus, mul, div : 사용할 수 있는 연산자의 개수 

  if index == len(a):
    return (cur, cur)

  res = []
  if plus > 0:
    res.append(calc(a, index+1, cur+a[index], plus-1, minus ,mul, div))
  if minus > 0:
    res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
  if mul > 0:
    res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
  if div > 0:
    if cur >= 0:
      res.append(calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
    else:
      res.append(calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
  
  
  ans = (
    max([t[0] for t in res]),
    min([t[1] for t in res])
  )

  return ans

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = calc(a, 1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])