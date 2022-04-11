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

n = int(input())
a = [i for i in range(1, n+1)]

print(' '.join(map(str, a)))

while next_permutation(a, n):
  print(' '.join(map(str, a)))



# from itertools import permutations

# n = int(input())
# l = [i for i in range(1, n+1)]

# for li in list(permutations(l)):
#   for el in li:
#     print(el, end=' ')
#   print()