import sys

# next permutation
# 1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다
# 2. j >= i 이면서 a[j] > a[i-1] 를 만족하는 가장 큰 j를 찾는다
# 3. a[i-1] 과 a[j]를 swap
# 4. a[i]부터 순열을 뒤집는다

n = int(input())
a = list(map(int, input().split()))

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


if next_permutation(a, n):
  print(' '.join(map(str, a)))
else:
  print(-1)

    