def solve(a, index, lotto):
  if len(lotto) == 6:
    print(" ".join(map(str, lotto)))
    return

  if index == len(a):
    return

  solve(a, index+1, lotto+[a[index]])
  solve(a, index+1, lotto)

while True:
  a = list(map(int, input().split()))
  if a[0] == 0:
    break

  a.pop(0)

  solve(a, 0, [])
  print()