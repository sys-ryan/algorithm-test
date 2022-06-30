n = int(input())

ans = 0
start = 1
end = 0
l = 1
while start <= n:
  end = start*10 - 1
  if end > n:
    end = n
  ans += (end - start + 1)*l

  start *= 10
  l += 1

print(ans)  