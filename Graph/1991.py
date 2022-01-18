class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right


n = int(input())
a = dict()
for _ in range(n):
  x, l, r = map(str, input().split())

  a[x] = Node(l, r)

def preorder(x):
  if x == '.':
    return
  print(x, end='')
  preorder(a[x].left)
  preorder(a[x].right)

def inorder(x):
  if x == '.':
    return
  inorder(a[x].left)
  print(x, end='')
  inorder(a[x].right)

def postorder(x):
  if x == '.':
    return 
  postorder(a[x].left)
  postorder(a[x].right)
  print(x, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
  