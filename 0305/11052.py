import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)

price = '0 ' + input()
price = list(map(int, price.split()))

for i in range(1, n+1):
  d[i] = price[i]

for i in range(2, n+1):
  for j in range(1, i+1):
    if d[i] < d[i-j] + price[j]:
      d[i] = d[i-j] + price[j]

print(d[n])

