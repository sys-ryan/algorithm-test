n = int(input())
t = [0]
p = [0]

for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

answer = 0
def go(day, total):
  global answer
  if day == n+1:
    answer = max(answer, total)
    return 

  if day > n+1:
    return

  go(day+1, total)
  go(day+t[day], total+p[day])

go(1, 0)

print(answer)


  