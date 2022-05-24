n = int(input())

t = []
p = []

for _ in range(n):
  a, b =  map(int, input().split())

  t.append(a)
  p.append(b)

answer = 0
def go(day, total):
  global answer

  if day == n:
    if total > answer:
      answer = total 

    return 

  if day > n:
    return 

  go(day+t[day], total+p[day])
  go(day+1, total)

go(0, 0)

print(answer)