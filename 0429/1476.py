e, s, m = map(int, input().split())

e -= 1
s -= 1
m -= 1

i = 0
while True:
  if i % 15 == e and i % 28 == s and i % 19 == m:
    print(i+1)
    break
  i += 1