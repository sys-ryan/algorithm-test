#수 이어 쓰기 1
import sys
input = sys.stdin.readline

n = int(input())
start = 1
len = 1
ans = 0
while start <= n:

  end = start*10 - 1
  if end > n:
    end = n
  ans += (end - start + 1) * len

  len += 1
  start *= 10

print(ans)
  