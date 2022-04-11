n, m = map(int, input().split())
answer = [0] * m

def go(index, start, n, m):
  if index == m:
    print(' '.join(map(str, answer)))
    return
  
  for i in range(start, n+1):
    answer[index] = i
    go(index+1, i+1, n, m)

go(0, 1, n, m)