def go(sum, goal):
  if sum > goal:
    return 0
  
  if sum == goal:
    return 1

  total = 0 
  for i in range(1, 4):
    total += go(sum+i, goal)
  
  return total

t = int(input())
for _ in range(t):
  n = int(input())
  print(go(0, n))
