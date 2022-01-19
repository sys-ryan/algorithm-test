n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
a = [0] * m

def go(index, start, n, m):
  if index == m:
    for el in a:
      print(num[el-1], end=' ')
    print()
    return

  for i in range(start, n+1):
    a[index] = i
    go(index+1, i+1, n, m)

go(0, 1, n, m)

