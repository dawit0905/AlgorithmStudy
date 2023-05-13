import sys


def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b - a) % 2 == 0:
        return 4
    else:
        return 3


def solve(num, left, right):
    if num >= len(arr)-1:
        return 0

    if dp[num][left][right] != 0:
        return dp[num][left][right]

    # dp[n][left][right] = min(solve(left, arr[n], n+1)+points[left][arr[n]], solve(arr[n], right, n+1)+points[right][arr[n]])
    dp[num][left][right] = min(solve(num+1, arr[num], right)+move(left, arr[num]), solve(num+1, left, arr[num])+move(right, arr[num]))
    return dp[num][left][right]


sys.setrecursionlimit(10**6)
arr = list(map(int, sys.stdin.readline().split()))
# points = {0:[0,2,2,2,2], 1: [0,1,3,4,3], 2:[0,3,1,3,4], 3:[0,4,3,1,3], 4:[0,3,4,3,1]}
dp = [[[0] * 5 for _ in range(5)] for _ in range(100000)]

print(solve(0,0,0))
