# n^2
# import sys
#
#
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
#
# dp = [1] * n
#
# for k in range(1, n):
#     for i in range(0, k):
#         if arr[i] > arr[k]:
#             dp[k] = max(dp[k], dp[i] + 1)
#
# print(n - max(dp))

# n log n
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
reverse_arr = list(map(int, sys.stdin.readline().split()))[::-1]

arr = []
for i in range(n):
    target = reverse_arr[i]
    idx = bisect_left(arr, target)

    if len(arr) == idx:
        arr.append(target)
    else:
        arr[idx] = target

print(n - len(arr))

