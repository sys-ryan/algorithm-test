#가장 긴 감소하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)
a = '0 '
a += input()
a = list(map(int, a.split()))

for i in range(1, n+1):
  d[i] = 1
  for j in range(1, i):
    if a[j] > a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
  

print(max(d))

