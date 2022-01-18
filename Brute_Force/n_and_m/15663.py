# #N과 M (9)
# import sys
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort()

# a = [0] * m
# cnt = [0] * 10

# for i in range(n):
#   cnt[num[i]] += 1

# print(cnt)
# def go(index, n, m):
#   if index == m:    
#     print(a)
#     temp = list(dict.fromkeys(a))
#     print(' '.join(map(str, temp)))
#     return
#   for i in range(n):
#     if cnt[num[i]] > 0:
#       cnt[num[i]] -= 1
#       a[index] = num[i]
#       go(index+1, n, m)
#       cnt[num[i]] += 1

# go(0, n, m)

import sys
from collections import Counter
n,m = map(int,input().split())
temp = list(map(int,input().split()))
# print(temp)
temp = list(Counter(temp).items())
# print(temp)
temp.sort()
print(temp)
n = len(temp)
num,cnt = map(list,zip(*temp))
# print(num)
# print(cnt)
a = [0]*m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        if cnt[i] > 0:
            cnt[i] -= 1
            a[index] = num[i]
            go(index+1, n, m)
            cnt[i] += 1
go(0,n,m)
