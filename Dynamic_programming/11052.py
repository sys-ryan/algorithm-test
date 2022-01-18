#카드 구매하기 (최댓값)
import sys
input = sys.stdin.readline

n = int(input())

p = '0 '
p += input()
p = list(map(int, p.split()))


d = [0] * 1001

# d[n] = max(d[n-i]+p[i]) 1 <= i <= n

d[0] = 0

for i in range(1, n+1):
  for j in range(1, i+1):
    d[i] = max(d[i], d[i-j] + p[j])

print(d[n])