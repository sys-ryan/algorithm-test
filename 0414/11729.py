def solve(n, x, y):
  pass
  
def solve(n, x, y):
  if n == 0:
    return
  
  solve(n-1, x, 6-x-y)
  print(f'{x} {y}')
  solve(n-1, 6-x-y, y)

n = int(input())
print(2**n-1)
solve(n, 1, 3)