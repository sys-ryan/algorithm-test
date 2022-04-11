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
a = [list(map(int, input().split())) for _ in range(n)]
d = list(range(n))

ans = -1

while True:
  ok = True
  s = 0
  for i in range(0, n-1):
    if a[d[i]][d[i+1]] == 0: #갈 수 없음
      ok = False
      break
    else: #갈 수 있음
      s += a[d[i]][d[i+1]]
  
  if ok and a[d[-1]][d[0]] != 0: # 마지막도시 -> 처음도시 갈 수 있음
    s += a[d[-1]][d[0]]
    if ans == -1:
      ans = s
    else:
      ans = min(ans, s)
    
  if not next_permutation(d, n):
    break
  if d[0] != 0: #시작 도시를 0으로 고정해서 진행 (0, 1, 2, 3 이나  1, 2, 3, 0 이나 비용 같음)
    break
    
print(ans)
  


