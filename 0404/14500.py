dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = 0

def go(x, y, sum, cnt):
  # (x ,y) 방문할지 결정 
  # sum: 여태까지 수의 합, cnt: 방문한 칸의 개수 

  if cnt == 4:
    global ans 
    if ans < sum:
      ans = sum
    return 
  
  if x  < 0 or x >= n or y < 0 or y >= m:
    return
  
  if c[x][y]:
    return

  c[x][y] = True
  for k in range(4):
    go(x+dx[k], y+dy[k], sum+a[x][y], cnt+1)
  c[x][y] = False

for i in range(n):
  for j in range(m):
    go(i, j, 0, 0)

    #T block은 재귀함수로 해결할 수 없기 때문에 for문으로 살펴본다
    if j+2 < m:
      temp = a[i][j] + a[i][j+1] + a[i][j+2]
      if i-1 >= 0:
        temp2 = temp + a[i-1][j+1]
        if ans < temp2:
          ans = temp2
      
      if i+1 < n:
        temp2 = temp + a[i+1][j+1]
        if ans < temp2:
          ans = temp2 
        
    if i+2 < n:
      temp = a[i][j] + a[i+1][j] + a[i+2][j]
      if j+1 < m:
        temp2 = temp + a[i+1][j+1]
        if ans < temp2:
          ans = temp2
    
      if j-1 >= 0:
        temp2 = temp + a[i+1][j-1]
        if ans < temp2:
          ans = temp2

print(ans)