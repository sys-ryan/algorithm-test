def possible(a, c, mid):
  cnt = 1
  last = a[0]
  for house in a:
    if house - last >= mid:
      cnt += 1
      last = house
  
  return cnt >= c


n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

ans = 1
l = 1
r = a[-1] - a[0]

while l <= r:
  mid = (l+r) // 2
  if possible(a, c, mid):
    ans = max(ans, mid)
    l = mid + 1
  else:
    r = mid - 1

print(ans)