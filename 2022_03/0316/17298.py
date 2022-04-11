import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = [0]
ans = [0] * n

for i in range(1, n):
  while stack and a[i] > a[stack[-1]]:
    ans[stack[-1]] = a[i]
    stack.pop()
  stack.append(i)

for i in range(n):
  if ans[i] == 0:
    ans[i] = -1 

answer = ' '.join(list(map(str, ans)))
print(answer)