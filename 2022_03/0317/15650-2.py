n, m = map(int, input().split())
a = [0] * m 

# index라는 수를 결과에 포함 O/X 결정 
def go(index, selected, n, m):
  if selected == m:
    print(' '.join(map(str, a)))
    return 

  if index > n:
    return 

  # index를 결과에 추가 
  # 사전순 증가하느 순서로 출력해야 하므로 포함되는 것 부터 처리
  a[selected] = index
  go(index+1, selected+1, n, m)
  
  # index를 결과에 추가하지 않음
  a[selected] = 0
  go(index+1, selected, n, m)

# 1 을 결과에 포함할지 말지 결정(여태까지 선택된 수의 길이[selected] = 0)
go(1, 0, n, m)