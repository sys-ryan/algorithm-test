from re import M
import sys
n, m = map(int, input().split())
# c = [False] * (n+1)
a = [0] * m

def go(index, start, n, m):
  if index == m:
    print(' '.join(map(str, a)))
    return

  for i in range(start, n+1):
    a[index] = i
    go(index+1, i+1, n, m)

go(0, 1, n, m)