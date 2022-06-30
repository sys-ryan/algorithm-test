n, m = map(int, input().split())

a = [0] * m
c = [False] * (n+1)

def go(index, start, n, m):
  if index == m:
    print(' '.join(map(str, a)))
    return
  
  for i in range(start, n+1):
    if c[i]:
      continue
    c[i] = True
    a[index] = i
    go(index+1, i+1, n, m)
    c[i] = False

go(0, 1, n, m)