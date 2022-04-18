import sys
input = sys.stdin.readline 

# 크리 size 인 블루레이로 녹화 -> m개 이하의 블루레이가 나오나? Yes/No
def go(a, m, size):
  cnt = 1
  total = 0

  for i in range(n):
    if total + a[i] > size: 
      cnt += 1
      total = a[i]
    else:
      total += a[i]
  return cnt <= m

n, m = map(int, input().split())
a = list(map(int, input().split()))

left = max(a) # 최소: 레슨 크기의 최댓값
right = sum(a) # 최대: 레슨 크기의 합

ans = 0
while left <= right:
  mid = (left + right) // 2
  if go(a, m, mid):
    ans = mid
    right = mid - 1
  else:
    left = mid + 1

print(ans)