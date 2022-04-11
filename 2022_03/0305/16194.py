import sys

input = sys.stdin.readline

n = int(input())

price = '0 ' + input()
price = list(map(int, price.split()))

d = [-1] * (n+1)
d[0] = 0

for i in range(1, n+1):
  for j in range(1, i+1):
    if d[i] == -1 or d[i] > d[i-j] + price[j]:
      d[i] = d[i-j] + price[j]

print(d[n])
