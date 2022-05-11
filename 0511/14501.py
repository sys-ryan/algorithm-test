



n = int(input())
t = []
p = []
ans = 0
for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)


def go(day, sum):
  global ans
  if day == n:
    if ans < sum:
      ans = sum
    return 

  if day > n:
    return 

  go(day+t[day], sum+p[day])
  go(day+1, sum)

go(0, 0)

print(ans)