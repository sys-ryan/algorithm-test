def merge(a, start, end):
  mid = (start + end) // 2
  i = start
  j = mid + 1
  k = 0
  b = [0] * (end-start+1)

  while i <= mid and j <= end:
    if a[i] < a[j]:
      b[k] = a[i]
      k += 1
      i += 1
    else:
      b[k] = a[j]
      k += 1
      j += 1
  
  while i <= mid:
    b[k] = a[i]
    k += 1
    i += 1
  
  while j <= end:
    b[k] = a[j]
    k += 1
    j += 1

  for i in range(start, end+1):
    a[i] = b[i-start]
      

def sort(a, start, end):
  if start == end:
    return
  mid = (start+end) // 2
  sort(a, start, mid)
  sort(a, mid+1, end)
  merge(a, start, end)

n = int(input())
a = [int(input()) for _ in range(n)]

sort(a, 0, n-1)
for el in a:
  print(el)