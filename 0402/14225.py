
n = int(input())
a = list(map(int, input().split()))
check = [False] * (n*100000 + 10)

def go(i, total):
  if i == n:
    check[total] = True
    return
  go(i+1, total+a[i])
  go(i+1, total)

go(0, 0)

i = 1
while True:
  if check[i] == False:
    break
  i += 1

print(i)