import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
  s = list(input())
  s.pop()
  board.append(s)

def check(board):
  length = len(board)
  max_len = 1
  for i in range(n):
    cnt = 1
    for j in range(1, n):
      if board[i][j] == board[i][j-1]:
        cnt += 1
      else:
        cnt = 1

      if cnt > max_len:
        max_len = cnt

    cnt = 1
    for j in range(1, n):
      if board[j][i] == board[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      
      if cnt > max_len:
        max_len = cnt

  return max_len
      
answer = 0
for i in range(n):
  for j in range(n):
    if j+1 < n:
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      temp = check(board)
      if answer < temp:
        answer = temp
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    
    if i+1 < n:
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      temp = check(board)
      if answer < temp:
        answer = temp
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)