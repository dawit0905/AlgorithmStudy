import sys


n = int(sys.stdin.readline())

dp = [0] * (n+1)
arr = [0] + list(map(int, sys.stdin.readline().split()))


for i in range(1, n+1):
    for j in range(1, i+1):
        if not dp[i]:
            dp[i] = dp[i-j] + arr[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + arr[j])

print(dp[n])
