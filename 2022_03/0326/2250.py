class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.order = 0
    self.depth = 0

n = int(input())
a = dict()
cnt = [0] * 100001
left = [0] * 100001
right = [0] * 100001
order = 0

def inorder(node, depth):
  global order
  if node == -1:
    return
  inorder(a[node].left, depth+1)
  order += 1
  a[node].order = order
  a[node].depth = depth
  inorder(a[node].right, depth+1)

for i in range(n):
  x, l, r = map(int, input().split())
  
  a[x] = Node(l, r)
  if l != -1:
    cnt[l] += 1
  if r != -1:
    cnt[r] += 1

# find root node
root = 0
for i in range(1, n+1):
  if cnt[i] == 0:
    root = i

inorder(root, 1)

max_depth = 0
for i in range(1, n+1):
  depth = a[i].depth
  order = a[i].order

  if left[depth] == 0:
    left[depth] = order
  else:
    left[depth] = min(left[depth], order)

  right[depth] = max(right[depth], order)
  
  max_depth = max(max_depth, depth)

answer = 0
answer_level = 0
for i in range(1, max_depth+1):
  if answer < right[i] - left[i] + 1:
    answer = right[i] - left[i] + 1
    answer_level = i

print(f'{answer_level} {answer}')

   

