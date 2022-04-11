n = int(input())
t = []
p = []

for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

ans = 0
def go(day, total):
  # day: day 일 에 일을 할지말지 결정하는 상황
  # total: 여태까지 번 돈 

  global ans 
  if day == n:
    ans = max(ans ,total)
    return
  
  if day > n:
    return
  
  # 일을 함 
  go(day+1, total)

  # 일을 안함
  go(day+t[day], total+p[day])


# 시작 일 0 이라고 정함
go(0, 0)
print(ans)