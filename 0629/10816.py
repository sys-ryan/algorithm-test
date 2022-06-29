def lower_bound(a, num):
  l = 0
  r = len(a) - 1

  ans = -1

  while l <= r:
    mid = (l+r)//2
    if a[mid] == num:
      ans = mid
      r = mid - 1
    elif a[mid] > num:
      r = mid-1
    else:
      l = mid+1
  return ans 

def upper_bound(a, num):
  l = 0
  r = len(a) - 1
  ans = -1

  while l <= r:
    mid = (l+r)//2
    if a[mid] == num:
      ans = mid
      l = mid+1
    elif a[mid] > num:
      r = mid - 1
    else:
      l = mid + 1
  return ans

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
  l = lower_bound(a, num)
  r = upper_bound(a, num)
  if l == -1:
    print('0', end=' ')
  else:
    print(r-l+1, end=' ')
print()