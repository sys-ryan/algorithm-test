n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

ans_cnt = 0
ans = 0
cnt = 1
for i in range(1, n):
  if a[i] == a[i-1]:
    cnt += 1
    if ans_cnt < cnt:
      ans_cnt = cnt
      ans = a[i]
  else:
    cnt = 1

print(ans)