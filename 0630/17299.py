n = int(input())
a = list(map(int, input().split()))

freq = [0] * (1000001)

for num in a:
  freq[num] += 1

stack = []
stack.append(0)

l = len(a)


answer = [0] * l
for i in range(1, l):
  if not stack:
    stack.append(i)
    continue

  while stack and freq[a[stack[-1]]] < freq[a[i]]:
    answer[stack[-1]] = a[i]
    stack.pop()
  stack.append(i)


while stack:
  answer[stack[-1]] = -1
  stack.pop()

print(' '.join(map(str, answer)))
