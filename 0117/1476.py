import sys

e, s, m = map(int, input().split())

e -= 1
s -= 1
m -= 1

a, b, c = 0, 0, 0
cnt = 1
while True:
  if a % 15 == e and b % 28 == s and c % 19 == m:
    print(cnt)
    break

  cnt += 1
  a += 1
  b += 1
  c += 1

  

