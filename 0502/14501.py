n = int(input())

t = [0]
p = [0]

for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)


ans = 0

def go(day, s):
  global ans
  if day == n+1:
    ans = max(ans, s)
    return
  if day > n+1:
    return
  
  go(day+1, s)
  go(day+t[day], s+p[day])

go(1, 0)
print(ans)