#포도주 시식


#d[i][0] : i 번째 잔 안마심 
#d[i][1] : i 번째 잔 마심   

import sys
input = sys.stdin.readline

n = int(input())

d = [[0]*2 for _ in range(n+1)]
a = [0]

for _ in range(n):
  a.append(int(input()))

if n == 1:
  print(a[1])
  sys.exit(0)
  
d[1][0] = 0
d[1][1] = a[1]
d[2][0] = a[1]
d[2][1] = a[1] + a[2]

for i in range(3, n+1):
  d[i][0] = max(d[i-1][0], d[i-1][1])
  d[i][1] = max(d[i-1][0], d[i-2][0] + a[i-1]) + a[i]

print(max(d[n]))