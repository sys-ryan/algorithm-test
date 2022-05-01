n, m = map(int, input().split())

a = [0] * m

def go(index, selected , n, m):
  # index 라는 수를 결과에 넣을지 말지 결정 (O, X)
  # selected: 지금까지 선택한 수의 개수 
  
  if selected == m:
    print(' '.join(map(str, a)))
    return
  
  if index > n:
    return 
  
  # index를 결과에 추가함
  a[selected] = index
  go(index+1, selected+1, n, m)

  # index를 결과에 추가하지 않음
  a[selected] = 0
  go(index+1, selected, n, m)

go(1, 0, n, m)