import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n

for i in range(n):
  d[i] = 1

for i in range(1, n):
  for j in range(i):
    if a[j] < a[i] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
      v[i] = j

# print(d, v)

def findMax():
  idx = 0
  max_val = 0
  for i in range(n):
    if d[i] > max_val:
      max_val = d[i]
      idx = i
  
  return idx, max_val

def track(p):
  if p == -1:
    return
  
  track(v[p])
  print(a[p], end=' ')


idx, max_val = findMax()
print(max_val)
track(idx)
print()