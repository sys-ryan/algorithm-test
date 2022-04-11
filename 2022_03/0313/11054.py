import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d_inc = [0] * n
d_dec = [0] * n

for i in range(n):
  d_inc[i] = 1
  for j in range(i):
    if a[j] < a[i] and d_inc[i] < d_inc[j] + 1:
      d_inc[i] = d_inc[j] + 1

for i in range(n-1, -1, -1):
  d_dec[i] = 1
  for j in range(i+1, n):
    if a[i] > a[j] and d_dec[i] < d_dec[j] + 1:
      d_dec[i] = d_dec[j] + 1

ans_arr = [0] * n
for i in range(n):
  ans_arr[i] = d_inc[i] + d_dec[i] - 1

print(max(ans_arr))
  
