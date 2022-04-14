from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def dist(p1: Point, p2: Point):
  return (p1.x-p2.x)**2 + (p1.y - p2.y)**2

def brute_force(a, start, end):
  ans = -1
  for i in range(start, end):
    for j in range(i+1, end+1):
      d = dist(a[i], a[j])
      if ans == -1 or ans > d:
        ans = d

  return ans

def closest(a, start, end):
  n = end-start+1
  if n <= 3:
    return brute_force(a, start, end)
  
  mid = (start + end) // 2
  left = closest(a, start, mid)
  right = closest(a, mid+1, end)
  ans = min(left, right)
  b = []
  for i in range(start, end+1):
    d = a[i].x - a[mid].x
    if d*d < ans:
      b += [a[i]]
  
  b.sort(key=lambda p: (p.y, p.x))
  m = len(b)
  for i in range(m-1):
    for j in range(i+1, m):
      y = b[j].y - b[i].y
      if y*y < ans:
        d = dist(b[i], b[j])
        if d < ans: 
          ans = d
      else:
        break

  return ans

n = int(input())
a = [Point(*map(int, input().split())) for _ in range(n)]
a.sort()
print(closest(a, 0, n-1))