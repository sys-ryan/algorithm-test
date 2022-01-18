import sys

n = int(input())
a = [list(input()) for _ in range(n)]

def check(a):
  ans = 0
  
  for i in range(n):
    cnt = 1  
    for j in range(n-1):
      if a[i][j] == a[i][j+1]:
        cnt += 1
      else:
        cnt = 1

      if ans < cnt:
          ans = cnt

    cnt = 1
    for j in range(n-1):
      
      if a[j][i] == a[j+1][i]:
        cnt += 1
      else:
        cnt = 1


      if ans < cnt:
          ans = cnt

      
  return ans

ans = 0
for i in range(n):
  for j in range(n-1):
    a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
    ans = max(ans, check(a))
    a[i][j], a[i][j+1] = a[i][j+1], a[i][j]

  for j in range(n-1):
    a[j][i], a[j+1][i] = a[j+1][i], a[j][i]
    ans = max(ans, check(a))
    a[j][i], a[j+1][i] = a[j+1][i], a[j][i]

  
print(ans)
