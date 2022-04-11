# 그룹의 크기: 감소 
# 그룹의 개수: 증가

n, m, k = map(int, input().split())
if m+k-1 <= n <= m*k:
  a = [i+1 for i in range(n)]
  g = [0, k] # g: 그룹의 경계
  n -= k
  m -= 1

  gs = 1 if m == 0 else n//m
  r = 0 if m ==0 else n%m
  for i in range(m):
    g += [g[-1] + gs + (1 if r > 0 else 0)]
    if r > 0:
       r -= 1

  for i in range(len(g) - 1):
    u = g[i]
    v = g[i+1]
    a[u:v] = a[u:v][::-1] # u~v 까지의 그룹 뒤집기 
  
  print(' '.join(map(str, a)))
  
else:
  print(-1)