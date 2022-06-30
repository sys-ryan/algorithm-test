n = int(input())
k = int(input())

left = 1
right = n*n

ans = 0

while left <= right:
  mid = (left+right) // 2
  cnt = 0

  for i in range(1, n+1):
    cnt += min(n, mid//i)
  if cnt >= k:
    ans = mid
    right = mid-1
  else:
    left = mid+1

print(ans)
