from re import X


t = int(input())

for _ in range(t):
  m, n, x, y = map(int, input().split())
  x -= 1
  y -= 1

  k = x

  ok = False
  while k < n*m:
    if k%n == y:
      print(k+1)
      ok = True
      break
    k += m
  
  if not ok:
    print(-1)