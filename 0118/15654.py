from re import I


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
check = [False] * (n+1)
a = [0] * m

def go(index, n, m):
  if index == m:
    for i in range(m):
      print(num[a[i]-1], end=' ')
    print()
    return

  for i in range(1, n+1):
    if check[i] == False:
      a[index] = i
      check[i] = True
      go(index+1, n, m)
      check[i] = False
      
go(0, n, m)


