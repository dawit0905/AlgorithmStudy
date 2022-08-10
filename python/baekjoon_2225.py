import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * 201 for _ in range(201)]
dp[0][0] = 1

for i in range(1, k+1):
    dp[i][1] = i
    for j in range(n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp[i][j] %= 1000000000

print(dp[k][n])
