import sys


t = int(sys.stdin.readline())
while t:
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    print(max(dp))
    t -= 1