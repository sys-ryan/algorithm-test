from collections import deque

# num 의 index th 수를 digit 으로 변경
def change(num, index, digit):
  if index == 0 and digit == 0:
    return -1
  s = list(str(num))
  s[index] = chr(digit+ord('0'))
  return int(''.join(s))

t = int(input())


# 에라토스테네스의 채
prime = [True] * 10001
for i in range(2, 10001):
  if prime[i] == True:
    for j in range(i*i, 10001, i):
      prime[j] = False

# for i in range(10001):
#   prime[i] = not prime[i]

for _ in range(t):
  n, m = map(int, input().split())
  check = [False] * 10001
  dist = [0] * 10001
  dist[n] = 0
  check[n] = True

  q = deque()
  q.append(n)
  while q:
    now = q.popleft()
    for i in range(4):
      for j in range(10):
        nxt = change(now, i, j)
        if nxt != -1:
          if prime[nxt] and check[nxt] == False:
            q.append(nxt)
            dist[nxt] = dist[now] + 1
            check[nxt] = True
  print(dist[m])
    