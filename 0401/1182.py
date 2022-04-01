n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, (1<<n)):

  s = 0
  for k in range(n):
    if i & (1<<k) > 0:
      s += a[k]
    
  if s == m:
    ans += 1
print(ans)