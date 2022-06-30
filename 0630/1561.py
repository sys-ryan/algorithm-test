p, n = map(int, input().split())
a = list(map(int, input().split()))

if p <= n:
  print(p)
  exit()

left = 0
right = 2000000000 + 1000000

while left <= right:
  mid = (left+right) // 2
  begin = 0
  end = n # 0초 처리   # mid 분에 타는 학생 [begine:end]

  for i in range(n):
    end += mid // a[i]
  
  begin = end
  for i in range(n):
    if mid % a[i] == 0:
      begin -= 1
  begin += 1

  if p < begin:
    right = mid-1
  elif p > end:
    left = mid + 1
  else:
    for i in range(n):
      if mid % a[i] == 0:
        if p == begin:
          print(i+1)
          exit()
        begin += 1