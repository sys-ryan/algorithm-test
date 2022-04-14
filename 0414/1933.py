from collections import namedtuple

Building = namedtuple('Building', ['left', 'height', 'right'])
Pair = namedtuple('Pair', ['x', 'height'])

def append(ans: list[Pair], p: Pair):
  if ans:
    if ans[-1].height == p.height:
      return
    if ans[-1].x == p.x:
      ans[-1] = Pair(ans[-1].x, p.height)
      return
  ans += [p]

def merge(l: list[Pair], r: list[Pair]):
  ans = []
  h1 = 0 #스카이라인 1의 현재 높이
  h2 = 0 #스카이라인 2의 현재 높이
  i = 0
  j = 0

  while i < len(l) and j < len(r):
    u = l[i]
    v = r[j]

    if u.x < v.x:
      x = u.x 
      h1 = u.height
      h = max(h1, h2)
      append(ans, Pair(x, h))
      i += 1
    else:
      x = v.x 
      h2 = v.height
      h = max(h1, h2)
      append(ans, Pair(x, h))
      j += 1
  
  while i < len(l):
    append(ans, l[i])
    i += 1
  
  while j < len(r):
    append(ans, r[j])
    j += 1
  
  return ans

def go(a: list[Building], start, end):
  if start == end: #빌딩 1개 
    return [
      Pair(a[start].left, a[start].height),
      Pair(a[start].right, 0)
    ]
  
  mid = (start + end) // 2
  l = go(a, start, mid)
  r = go(a, mid+1, end)

  return merge(l, r)


n = int(input())
a = [Building(*map(int, input().split())) for _ in range(n)]
a.sort()
ans = go(a, 0, n-1)

for x, height in ans:
  print(f'{x} {height}', end=' ')
print()