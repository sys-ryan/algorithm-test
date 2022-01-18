#가장 큰 증가하는 부분수열 
import sys
input = sys.stdin.readline

n = int(input())

a = '0 '
a += input()
a = list(map(int, a.split()))

d = [0] * (n+1)

for i in range(1, n+1):
  d[i] = a[i]
  for j in range(1, i+1):
    if a[j] < a[i] and d[i] < d[j] + a[i]:
      d[i] = d[j] + a[i]
  
print(max(d))


