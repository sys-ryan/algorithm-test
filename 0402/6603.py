# go(a, index, cnt)
# a: 입력으로 주어진 수 
# index: 선택할지 말지 결정해야 하는 인덱스
# cnt: 현재까지 포함한 수의 개수 

def solve(a, index, lotto):
  if len(lotto) == 6:
    print(' '.join(map(str, lotto)))
    return
  if index == len(a):
    return
  
  solve(a, index+1, lotto+[a[index]])
  solve(a, index+1, lotto)

while True: 
  input_str = list(map(int, input().split()))
  k = input_str[0]

  if k == 0:
    break

  a = []
  for i in range(1, k+1):
    a.append(input_str[i])

  solve(a, 0, [])
  print()
  

