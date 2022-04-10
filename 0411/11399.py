n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
total = 0
for i in range(n):
  total += a[i]
  ans += total


print(ans)   