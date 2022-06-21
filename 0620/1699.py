n = int(input())

d = [100001] * (n+1)
d[0] = 0
d[1] = 1
for i in range(1, n+1):
  # d[i] = i
  j = 1
  while j*j <= i:
    # print(i, j, d[i], d[i-j*j]+1, i-j*j)
    if d[i] > d[i-j*j] + 1:
      d[i] = d[i-j*j] + 1
    # print(d)
    j += 1
# print(d)
print(d[n])