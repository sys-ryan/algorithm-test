from re import L
import sys

def next_permutation(a, n):
  i = n-1
  while i > 0 and a[i-1] >= a[i]: #1
    i -= 1
  if i <= 0: #입력받은 수열이 마지막 순열인 경우
    return False 
  
  j = n-1 #2
  while a[j] <= a[i-1]:
    j -= 1
  a[i-1], a[j] = a[j], a[i-1] #3

  j = n-1 #4
  while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1
  return True

def print_ans(s, a, k):
  ans = []
  for i in range(k):
    if a[i] == 1:
      ans.append(s[i])

  return ans

while True:
  t = list(map(int, input().split()))

  k = t[0]

  if k == 0:
    sys.exit(0)

  s = []
  for i in range(1, k+1):
    s.append(t[i])

  a = [0] * (k - 6) + [1] * 6
  ans = []
  ans.append(print_ans(s, a, k))

  while next_permutation(a, k):
    ans.append(print_ans(s, a, k))
  
  ans.sort()
  for v in ans:
    print(' '.join(map(str, v)))

  print()
  

  

  