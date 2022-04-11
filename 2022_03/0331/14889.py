def go(index, first, second):
  # index th 사람을 어떤 팀에 넣을지 결정 
  # 1번 팀과 2번 팀에 속한 사람이 각각 frist, second 에 들어 있음

  # 정답을 찾은 경우 (index == n)
  if index == n:
    # 불가능한 경우 //back tracking
      # fisrt 의 크기 > n/2
      # second 의 크기 > n/2
    if len(first) != n//2 or len(second) != n//2:
      return -1
    
    # t1, t2 : team 1, team 2 의 능력치 
    t1 = 0
    t2 = 0
    for i in range(n//2):
      for j in range(n//2):
        if i == j:
          continue
        t1 += s[first[i]][first[j]]
        t2 += s[second[i]][second[j]]
    return abs(t1 - t2)
  
  ans = -1
  t1 = go(index+1, first+[index], second)
  if ans == -1 or (t1 != -1 and ans > t1):
    ans = t1
  t2 = go(index+1, first, second+[index])
  if ans == -1 or (t2 != -1 and ans > t2):
    ans = t2
  
  return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

print(go(0, [], []))