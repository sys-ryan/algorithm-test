import sys
input = sys.stdin.readline

def go(a, m, size):
  cnt = 1
  total = 0
  for i in range(n):
    if total + a[i] > size: # 크기를 넘어가면 새로운 블루레이 
      cnt += 1
      total = a[i]
    else:
      total += a[i] # 크기 안넘어가면 녹화 
  return cnt <= m

n, m = map(int, input().split())
a = list(map(int, input().split()))

left = max(a)
right = sum(a)

ans = 0
while left <= right:
  mid = (left + right) // 2
  if go(a, m, mid):
    ans = mid
    right = mid-1
  else:
    left = mid+1

print(ans)