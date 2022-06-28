n = int(input())
a = sorted(map(int, input().split()))

accumulate = 0
answer = 0

for x in a:
  accumulate += x
  answer += accumulate

print(answer)
