def go(a, index, r, c, size):
  # index 번째 글자를 찾아야 함
  # 가장 왼쪽 위 칸은 r행 c열 
  # 변의 길이는 size

  if size == 1:
    return (r, c)
  else:
    m = size//2
    if a[index] == '1':
      return go(a, index+1, r, c+m, m) # 1 사분면 
    elif a[index] == '2':
      return go(a, index+1, r, c, m) # 2 사분면
    elif a[index] == '3':
      return go(a, index+1, r+m, c, m) # 3 사분면
    elif a[index] == '4':
      return go(a, index+1, r+m, c+m, m) # 4 사분면
  return (0, 0)

def gogo(r, c, size, x, y):
  if size == 1:
    return ''
  
  m = size//2
  if x < r+m and y < c+m:
    return '2' + gogo(r, c, m, x, y)
  elif x < r+size//2 and y >= c+m:
    return '1' + gogo(r, c+m, m, x, y)
  elif x >= r+size//2 and y < c+m:
    return '3' + gogo(r+m, c, m, x, y)
  else:
    return '4' + gogo(r+m, c+m, m, x, y)

n, a = input().split()
n = int(n)
size = 2**n

x, y = go(a, 0, 0, 0, size)
dc, dr = map(int, input().split())
dr = -dr

x += dr
y += dc

if 0 <= x < size and 0 <= y < size:
  print(gogo(0, 0, size, x, y))
else:
  print(-1)