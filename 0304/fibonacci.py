def fibonacci_recursive(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input())
result = fibonacci_recursive(n)
print(result)


# Dynamic Programming
## Top-down 
memo = [0] * 100
def fibonacci_dp(n):
  if n <= 1:
    return n
  else:
    if memo[n] > 0:
      return memo[n]
    memo[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)
    return memo[n]

result_2 = fibonacci_dp(n)
print(result_2)


## Bottom-up
d = [0] * 100
def fibonacci_dp_bu(n):
  d[0] = 0
  d[1] = 1
  for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]
  
  return d[n]

print(fibonacci_dp_bu(n))