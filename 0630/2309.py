a = [int(input()) for _ in range(9)]
a.sort()

total = sum(a)

for i in range(9):
  for j in range(i+1, 9):
    if total - a[i] - a[j] == 100:
      for k in range(9):
        if k == i or k == j:
          continue
        print(a[k])
      exit()