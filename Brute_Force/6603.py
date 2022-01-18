#로또 
import sys

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

while True:
  l = list(map(int, input().split()))

  k = l[0]
  s = []
  for i in range(1, k+1):
    s.append(l[i])

  if k == 0:
    sys.exit(0)

  d = [0] * (k-6) + [1] * 6
  ans = []

  while True:
    cur = [s[i] for i in range(k) if d[i] == 1]
    ans.append(cur)

    if not next_permutation(d):
      break
  ans.sort()

  for v in ans:
    print(' '.join(map(str, v)))
  print()
