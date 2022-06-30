def check(a, mid, m):
  total = 0

  for i in range(len(a)):
    if a[i] - mid > 0:
      total += a[i] - mid
  return total >= m

n, m = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = max(a)
ans = 0

while l <= r:
  mid = (l+r) // 2
  if check(a, mid, m):
    ans = max(ans, mid)
    l = mid+1
  else:
    r = mid-1

print(ans)