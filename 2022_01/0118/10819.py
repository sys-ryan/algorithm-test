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

def calc(a, n):
  ans = 0
  for i in range(1, n):
    ans += abs(a[i] - a[i-1])
  return ans    

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = calc(a, n)
while next_permutation(a, n):
  ans = max(ans, calc(a, n))

print(ans)


