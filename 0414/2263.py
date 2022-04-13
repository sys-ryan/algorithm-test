import sys
sys.setrecursionlimit(10000000)

def solve(postorder, position, in_start, in_end, post_start, post_end):
  if in_start > in_end or post_start > post_end:
    return
  
  root = postorder[post_end]
  print(root, end=" ")
  p = position[root]

  left = p - in_start #왼쪽 자식의 수 
  solve(postorder, position, in_start, p-1, post_start, post_start + left - 1)
  solve(postorder, position, p+1, in_end, post_start + left, post_end - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n+1)
# position[i] : i번 정점이 inorder에서 몇 번째 index 인지 
# inorder[position[i]] = i

for i in range(n):
  position[inorder[i]] = i

solve(postorder, position, 0, n-1, 0, n-1)
print()