n, m = map(int, input().split())

check = [False] * (n+1)
answer = [0] * m 

def go(index, start, n, m):
  if index == m:
    print(' '.join(map(str, answer)))
    return
  
  for i in range(start, n+1):
    if check[i]:
      continue
    # check[i] = True
    answer[index] = i
    go(index+1, i+1, n, m)
    # check[i] = False

go(0, 1, n, m)
    