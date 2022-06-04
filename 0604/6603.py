
lotto = []
def go(a, index, cnt):
  if cnt == 6:
    print(' '.join(map(str, lotto)))
    return
  
  if len(a) == index:
    return 
  
  lotto.append(a[index])
  go(a, index+1, cnt+1)

  lotto.pop()
  go(a, index+1, cnt)


while True:
  a = list(map(int, input().split()))

  if a[0] == 0:
    break

  a = a[1:]

  go(a, 0, 0)
  print()
