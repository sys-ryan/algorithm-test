import math

def dist(x1, y1, z1, x2, y2, z2):
  return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

x1, y1, z1, x2, y2, z2, x3 ,y3, z3 = map(float, input().split())
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1
left = 0.0
right = 1.0

m = 0

while True:
  if abs(right-left) < 1e-9:
    m = (left+right) / 2
    break
  
  m1 = left + (right - left) / 3
  m2 = right - (right - left) / 3
  m1x = x1 + m1*dx
  m1y = y1 + m1*dy
  m1z = z1 + m1*dz
  m2x = x1 + m2*dx
  m2y = y1 + m2*dy
  m2z = z1 + m2*dz

  d1 = dist(m1x, m1y, m1z, x3, y3, z3)
  d2 = dist(m2x, m2y, m2z, x3, y3, z3)

  if d1 > d2:
    left = m1
  else:
    right = m2

x0 = x1 + m*dx
y0 = y1 + m*dy
z0 = z1 + m*dz

ans = dist(x0, y0, z0, x3, y3, z3)
print('%.10f'%ans)