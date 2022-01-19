n, m = map(int, input().split())
a = [0] * m

#index라는 수를 결과 에 포함 O/X 결정 
def go(index, selected, n, m): # index: 자연수, selected: 지금까지 선택한 수의 개수
  if selected == m:
    print(' '.join(map(str, a)))
    return

  if index > n:
    return
  
  # index를 결과에 추가
  #사전순 증가하는 순서로 출력이므로 1이 먼저 포함되는것부터 처리
  a[selected] = index
  go(index+1, selected+1, n, m)

  # index를 결과에 추가하지 않음
  a[selected] = 0
  go(index+1, selected, n, m)


go(1, 0, n, m)