n, m = map(int, input().split())
answer = [0] * m

def go(index, selected, n, m):
  if selected == m:
    print(' '.join(map(str, answer)))
    return 
  
  if index > n:
    return

  answer[selected] = index
  go(index+1, selected+1, n ,m)

  answer[selected] = 0
  go(index+1, selected, n, m)

go(1, 0, n ,m)
