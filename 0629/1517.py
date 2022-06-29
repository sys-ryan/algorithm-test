def solve(a, start, end):
  if start == end:
    return 0

  mid = (start + end) // 2
  b = [0]*(end-start+1)

  ans = solve(a, start, mid) + solve(a, mid+1, end)

  i = start
  j = mid+1
  k = 0

  while i <= mid and j <= end:
    if a[i] <= a[j]:
      b[k] = a[i]
      k += 1
      i += 1
    else:
      b[k] = a[j]
      k += 1
      j += 1
      ans += (mid - i + 1)
  
  while i <= mid:
    b[k] = a[i]
    k += 1
    i += 1
  while j <= end:
    ans += (mid - i + 1)
    b[k] = a[j]
    k += 1
    j += 1
  
  return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(a, 0, n-1))

