def check(a, m, x):
  cnt = 0
  for i in range(len(a)):
    cnt += a[i] // x
  return cnt >= m

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
l = 1
r = max(a)
while l <= r:
  mid = (l+r)//2
  if check(a, m, mid):
    ans = max(ans, mid)
    l = mid+1
  else:
    r = mid-1
print(ans)