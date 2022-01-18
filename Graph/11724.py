#연결 요소의 개수 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]


for _ in range(m):
  u, v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)

for i in range(1, n+1):
  a[i].sort()

check = [False] * (n+1)
def dfs(x):
  check[x] = True
  
  for y in a[x]:
    if check[y] == False:
      dfs(y)

cnt = 0
for i in range(1, n+1):
  if check[i] == False:
    dfs(i)
    cnt += 1

print(cnt)
