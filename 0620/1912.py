n = int(input())
a = [0] + list(map(int, input().split()))

d = [-2000] * (n+1)

for i in range(1, n+1):
  d[i] = a[i] 

  if i-1 == 0:
    continue
  
  d[i] = max(a[i], d[i-1] + a[i])

print(max(d))

