n = 9
a = [int(input()) for _ in range(n)]
total = sum(a)

a.sort()

for i in range(n):
  for j in range(i+1, n):
    if total - a[i] - a[j] == 100:
      for k in range(n):
        if k == i or k == j:
          continue
        print(a[k])
      exit()