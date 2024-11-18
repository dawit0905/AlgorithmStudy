import sys

from bisect import bisect_left
from bisect import bisect_right


n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))


for i in m_list:
    left = 0
    right = n - 1

    left_index = bisect_left(n_list, i)
    right_index = bisect_right(n_list, i)

    if left_index != -1:
        print(right_index-left_index)
    else:
        print(0)


def lower_bound(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right


def upper_bound(array, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return right

