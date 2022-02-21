# import sys
#
# n = int(sys.stdin.readline())
# n_arr = list(map(int, sys.stdin.readline().split()))
# n_arr.sort()
#
# m = int(sys.stdin.readline())
# m_arr = list(map(int, sys.stdin.readline().split()))
#
# answer = [0] * m
#
# for i in range(m):
#     start = 0
#     end = n-1
#
#     while start <= end:
#         mid = (start+end) // 2
#
#         if n_arr[mid] == m_arr[i]:
#             answer[i] = n_arr[start:end+1].count(m_arr[i])
#             break
#         elif n_arr[mid] >= m_arr[i]:
#             end = mid - 1
#         else:
#             start = mid + 1
#
# print(*answer)

from bisect import bisect_left, bisect_right
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))
card.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value) # 해당수가 있는 오른쪽 인덱스
    left_index = bisect_left(a, left_value) # 해당수가 있는 왼쪽 인덱스
    return right_index - left_index


for i in range(len(test)):
    print(count_by_range(card, test[i], test[i]), end=' ')