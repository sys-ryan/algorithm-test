import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())

  d = [[0, 0, 0] for _ in range(n)]
  a = [[0, 0] for _ in range(n)]

  # input a[]
  line_1 = list(map(int, input().split()))
  line_2 = list(map(int, input().split()))

  for i in range(n):
    a[i][0] = line_1[i]
    a[i][1] = line_2[i]

  d[0][0] = 0 
  d[0][1] = a[0][0]
  d[0][2] = a[0][1]

  for i in range(1, n):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = max(d[i-1][0], d[i-1][2]) + a[i][0]
    d[i][2] = max(d[i-1][0], d[i-1][1]) + a[i][1]


  print(max(d[n-1]))
