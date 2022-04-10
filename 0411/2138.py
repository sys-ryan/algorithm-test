def change(a, index):
  for i in range(index-1, index+2):
    if 0 <= i < len(a):
      a[i] = 1-a[i]

def go(a, goal):
  n = len(a)
  ans = 0
  for i in range(n-1):
    if a[i] != goal[i]:
      change(a, i+1)
      ans += 1
  
  ok = True
  for i in range(n):
    if a[i] != goal[i]:
      ok = False
    
  if ok:
    return (True, ans)
  else:
    return (False, ans)


n = int(input())
a = list(map(int, input()))
b = a[:]
goal = list(map(int, input()))

# 0th switch 안누름
p1 = go(b, goal)

# 0th switch 누름
change(a, 0)
p2 = go(a, goal)

if p2[0]:
  p2 = (p2[0], p2[1] + 1) # 0th 누른거 한번 count 해줌

if p1[0] and p2[0]:
  print(min(p1[1], p2[1]))
elif p1[0]:
  print(p1[1])
elif p2[0]:
  print(p2[1])
else:
  print(-1)