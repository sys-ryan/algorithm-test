import sys
n = int(input())

d = [0] * (n+1)

if n == 1:
   print(0)
   sys.exit()
   
if n <= 3:
  print(1)
  sys.exit()

d[0] = 0
d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, n+1):
  d[i] = d[i-1] + 1

  if i % 2 == 0:
    if d[i] > d[i//2] + 1:
      d[i] = d[i//2] + 1
  if i % 3 == 0:
    if d[i] > d[i//3] + 1:
      d[i] = d[i//3] + 1
  
print(d[n])