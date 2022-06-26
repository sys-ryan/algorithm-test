import sys
a = [int(input()) for _ in range(9)]

a.sort()

total = sum(a)

for i in range(9):
  for j in range(i+1, 9):
    if total - a[i] - a[j] == 100:
      for h in a:
        if h != a[i] and h != a[j]:
          print(h)
      sys.exit(0)
