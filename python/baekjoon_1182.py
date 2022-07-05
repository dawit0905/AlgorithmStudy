import sys
from itertools import combinations


'''
풀이법
1. 조합으로 가능한 조합들의 S를 구한다 - 성공
2. 재귀로 풀기 - 성공
'''

# 풀이법 1
# n, s = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# combi = []
# for i in range(1, n+1):
#     temp = list(combinations(arr, i))
#     # print(temp)
#     combi.extend(temp)
#
# cnt = 0
# for i in combi:
#     if sum(i) == s:
#         cnt += 1
#
# print(cnt)

# 풀이법 2
def func(curr, _sum):
    global cnt
    if curr == n:
        if _sum == s:
            cnt += 1
        return
    func(curr+1, _sum)
    func(curr+1, _sum+arr[curr])


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
func(0, 0)
if s == 0:
    cnt -= 1
print(cnt)
