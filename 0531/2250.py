class Node:
  def __init__(self, left, right, order, depth):
    self.left = left
    self.right = right
    self.order = order
    self.depth = depth

a = dict()
cnt = [0] * 10001
left = [0] * 10001
right = [0] * 10001

order = 0
def inorder(x, depth):
  global order
  if x == -1:
    return
  inorder(a[x].left, depth+1)
  order += 1
  a[x].order = order
  a[x].depth = depth
  inorder(a[x].right, depth+1)

n = int(input())
for _ in range(n):
  x, y, z = map(int, input().split())

  if y != -1:
    cnt[y] += 1
  if z != -1:
    cnt[z] += 1
  
  a[x] = Node(y, z, 0, 0)

root = 0
for i in range(1, n+1):
  if cnt[i] == 0:
    root = i

inorder(root, 1)

maxdepth = 0

for i in range(1, n+1):
  depth = a[i].depth
  order = a[i].order

  if left[depth] == 0:
    left[depth] = order
  else:
    left[depth] = min(left[depth], order)
  
  right[depth] = max(right[depth], order)
  maxdepth = max(maxdepth, depth)

ans = 0
ans_level = 0

for i in range(1, maxdepth+1):
  if ans < right[i] - left[i] + 1:
    ans = right[i] - left[i] + 1
    ans_level = i

print(f'{ans_level} {ans}')