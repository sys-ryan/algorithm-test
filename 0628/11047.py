n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0

for i in range(n-1, -1, -1):
  ans += k//a[i]
  k %= a[i]

print(ans)