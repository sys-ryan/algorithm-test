import sys
n = int(input())

d = [-1] * (n+1)

if n == 1:
  print(0)
  sys.exit(0)
elif n == 2:
  print(1)
  sys.exit(0)


d[1] = 0
d[2] = 1

for i in range(3, n+1):
  
  if i-1 >= 1:
    if d[i] == -1 or d[i] > d[i-1] + 1:
      d[i] = d[i-1] + 1

  if i%3 == 0:
    if d[i] == -1 or d[i] > d[i//3] + 1:
      d[i] = d[i//3] + 1

  if i%2 == 0:
    if d[i] == -1 or d[i] > d[i//2] + 1:
      d[i] = d[i//2] + 1


print(d[n])


