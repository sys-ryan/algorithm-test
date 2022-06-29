s = list(input())
s = [ord(ch) - ord('0') for ch in s]

total = sum(s)
s.sort()

if s[0] == 0 and total % 3 == 0:
  print(''.join(map(str, s[::-1])))
else:
  print(-1)