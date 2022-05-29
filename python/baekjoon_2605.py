# import sys
#
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# answer = [0] * n
# for i in range(1, n+1):
#     answer.insert(arr[i-1],i)
# answer.reverse()
# for i in answer:
#     if i != 0:
#         print(i, end=" ")

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = []

cnt = 1
for i in arr:
    result.insert(i, cnt)
    cnt += 1

result.reverse()
print(*result)
