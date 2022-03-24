import sys

n = int(sys.stdin.readline())
dp = [1, 1, 2] + [0] * 97

for i in range(3, n):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1])