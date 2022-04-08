import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(board, check, x, y):
  # (x,y) 에서 이동을 시작하고, 방문한 알파벳이 check일 때, 방문할 수 있는 칸의 최대 개수 

  # check: 방문한 알파벳
  # x, y: 현재 위치 
  # return value: 방문할 수 있는 최대 칸의 개수 

  n = len(board)
  m = len(board[0]) - 1

  ans = 0
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      ch = ord(board[nx][ny]) - ord('A')
      if not check[ch]:
        check[ch] = True
        temp = go(board, check, nx, ny)
        
        if ans < temp:
          ans = temp
        check[ch] = False

  return ans+1

  
n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]
check = [False]*26

check[ord(board[0][0]) - ord('A')] = True
print(go(board, check, 0, 0))