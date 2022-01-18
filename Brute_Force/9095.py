#1, 2, 3 더하기 (brute-force)

import sys

def go(sum, goal):
  if sum > goal:
    return 0
  if sum == goal:
    return 1
  
  now = 0

  for i in range(1, 3+1):
    now += go(sum+i, goal)
  
  return now


t = int(input())
for _ in range(t):
  n = int(input())
  print(go(0, n))
