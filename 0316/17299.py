import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

freq = [0] * 1000001

for num in a:
  freq[num] += 1

stack = [0]
ans = [0] * n

for i in range(1, n):
  while stack and freq[a[i]] > freq[a[stack[-1]]]:
    ans[stack[-1]] = a[i]
    stack.pop()
  stack.append(i)

for i in range(n):
  if ans[i] == 0:
    ans[i] = -1

print(' '.join(list(map(str, ans))))