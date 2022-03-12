import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d_start = [0] * n
d_end = [0] * n


for i in range(n):
  d_end[i] = a[i]
  if i == 0:
    continue
  if d_end[i] < d_end[i-1] + a[i]:
    d_end[i] = d_end[i-1] + a[i]

for i in range(n-1, -1, -1):
  d_start[i] = a[i]
  if i == n-1:
    continue
  if d_start[i] < d_start[i+1] + a[i]:
    d_start[i] = d_start[i+1] + a[i]


ans = d_end[0]
for i in range(1, n):
  if ans < d_end[i]:
    ans = d_end[i]

for i in range(1, n-1):
  if ans < d_end[i-1] + d_start[i+1]:
    ans = d_end[i-1] + d_start[i+1]

print(ans)