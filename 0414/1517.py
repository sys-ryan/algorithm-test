def solve(a, start, end):
  if start == end:
    return 0
  mid = (start+end) // 2
  b = [0] * (end-start+1)
  ans = solve(a, start, mid) + solve(a, mid+1, end)
  i = start
  j = mid+1
  k = 0

  while i <= mid or j <= end:
    if i <= mid and (j > end or a[i] <= a[j]):
      b[k] = a[i]
      k += 1
      i += 1
    else:
      ans += (mid - i + 1) # 오른쪽 수가 b에 들어갈때마다, 왼쪽에 남아있는 수의 개수를 더해준다 
      b[k] = a[j]
      k += 1
      j += 1

  for i in range(start, end+1):
    a[i] = b[i-start]
  
  return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(a ,0, n-1))