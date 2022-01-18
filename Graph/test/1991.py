class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right

a = dict()

n = int(input())

for _ in range(n):
  x, left, right = map(str, input().split())
  a[x] = Node(left, right)

def preorder(x):
  if x == '.':
    return
  print(x, end='')
  preorder(a[x].left)
  preorder(a[x].right)

preorder('A')
print()

