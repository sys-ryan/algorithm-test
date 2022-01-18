# 가장 긴 증가하는 부분 수열 (LIS)
import sys

n = int(input())
a = list(map(int, input().split()))

d = [0] * (n)

for i in range(0, n):
  d[i] = 1
  for j in range(0, i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1

print(max(d))