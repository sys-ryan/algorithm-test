n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
def go(i, total):
  global ans 

  if i == n:
    if total == s:
      ans += 1
    return

  go(i+1, total+a[i])
  go(i+1, total)

go(0 ,0)
if s == 0:
  ans -= 1
  
print(ans)