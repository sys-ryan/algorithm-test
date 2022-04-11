
def flip(x):
  if x == 'H':
    return 'T'
  else:
    return 'H'


n = int(input())
a = [list(map(str, input())) for _ in range(n)]

ans = n*n
for state in range(1<<n):
  total = 0 
  for j in range(n):
    cnt = 0 #t 의 개수
    for i in range(n):
      cur = a[i][j]
      if (state & (1<<i)) != 0: # i 행 flip 한 상태 
        cur = flip(cur)
      
      if cur == 'T':
        cnt += 1
    total += min(cnt, n-cnt)
  
  if ans > total:
    ans = total

print(ans)