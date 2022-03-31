def go(total, goal):
  if total > goal:
    return 0
  if total == goal:
    return 1
  now = 0
  for i in range(1, 4):
    now += go(total+i, goal)
  return now

t = int(input())

for _ in range(t):
  n = int(input())
  print(go(0, n))