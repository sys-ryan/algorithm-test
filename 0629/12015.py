def lower_bound(a, n, key):
  left = 0
  right = n
  while left < right:
    mid = (left+right) // 2
    if key <= a[mid]:
      right = mid
    else:
      left = mid+1

  return left

n = int(input())
a = [0]*n

nums = list(map(int, input().split()))

length = 0
for num in nums:
  p = lower_bound(a, length, num)
  a[p] = num
  if length == p:
    length += 1
print(length)