#외판원 순회2
import sys
from itertools import permutations

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
d = list(range(n))
perm = list(map(list, permutations(d)))
ans = -1
# print(w)

for p in perm:
  # print(p)
  ok = True
  s = 0
  for i in range(0, n-1):
    if w[p[i]][p[i+1]] == 0:
      ok = False
      break
    else:
      s += w[p[i]][p[i+1]]
  if ok and w[p[-1]][p[0]] != 0:
    s += w[p[-1]][p[0]]
    if ans == -1:
      ans = s
    else:
      ans = min(ans, s)
  
print(ans)
  