e, s, m = map(int, input().split())

x = 1
y = 1
z = 1
cnt = 1
while True:
  if x == e and y == s and z == m:
    print(cnt)
    break

  x += 1
  y += 1
  z += 1

  if x == 16:
    x = 1
  
  if y == 29:
    y = 1
  
  if z == 20:
    z = 1
  
  cnt += 1

  