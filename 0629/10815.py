def binary_search(a, num):
  l = 0
  r = len(a) - 1

  ans = -1

  while l <= r:
    mid = (l+r)//2
    if a[mid] == num:
      return True
    elif a[mid] > num:
      r = mid-1
    else:
      l = mid+1
  return False

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
nums = list(map(int, input().split()))
for num in nums:
  res = binary_search(a, num)
  print(int(res), end=' ')
print()
