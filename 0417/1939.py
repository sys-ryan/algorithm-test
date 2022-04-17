import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def go(a, check, node, limit):
  if check[node]:
    return False
  check[node] = True
  if node == end:
    return True
  for nxt, cost in a[node]:
    if cost >= limit:
      if go(a, check, nxt, limit):
        return True
  return False

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u, v, c = map(int, input().split())
  a[u].append((v, c))
  a[v].append((u, c))

start, end = map(int, input().split())
left = 1
right = 1000000000
ans = 0

while left <= right:
  mid = left + (right - left) // 2
  check = [False] * (n+1)
  if go(a, check, start, mid):
    ans = mid
    left = mid+1
  else:
    right = mid-1

print(ans)