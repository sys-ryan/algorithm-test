n = int(input())
a = list(map(int, input().split()))
c = [False] * (n*100000 + 10)

def go(i, s):
  if i == n:
    c[s] = True
    return

  go(i+1, s+a[i])
  go(i+1, s)

go(0, 0)

i = 1
while True:
  if c[i] == False:
    break
  i += 1

print(i)
    