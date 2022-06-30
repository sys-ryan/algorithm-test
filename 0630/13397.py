def go(a, mid):
  n = len(a)
  t1 = a[0]
  t2 = a[0]
  ans = 1

  for i in range(1, n):
    if t1 > a[i]:
      t1 = a[i]
    if t2 < a[i]:
      t2 = a[i]
    if t2 - t1 > mid:
      ans += 1
      t1 = a[i]
      t2 = a[i]
  return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = max(a)

ans = r

while l <= r:
  mid = (l+r) // 2
  if go(a, mid) <= k:
    r = mid-1
    if ans > mid:
      ans = mid
  else:
    l = mid+1
print(ans)
    