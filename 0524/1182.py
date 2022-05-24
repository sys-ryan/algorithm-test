n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, (1<<n)):
  total = 0

  for k in range(n):
    if i & (1<<k):
      total += a[k]
  
  if total == s:
    ans += 1

print(ans)
