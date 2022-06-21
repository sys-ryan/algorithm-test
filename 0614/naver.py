def solution(arr):
  nums = []
  for el in arr:
    if el not in nums:
      nums.append(el)
  
  # print(nums)
  answer = []
  for n in nums:
    cnt = arr.count(n)
    if cnt != 1:
      answer.append(cnt)
  
  if answer:
    print(answer)
  else:
    print([-1])



solution([1, 2, 3, 3, 3, 3, 4, 4])
solution([3, 2, 4, 4, 2, 5, 2, 5, 5])
solution([3, 5, 7, 9, 1])