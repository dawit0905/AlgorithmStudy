import sys


n, k = map(int, sys.stdin.readline().split())

dp = [[0] * (i+2) for i in range(31)]

for i in range(0, 31):
    for j in range(1, i+1):
        if j == 1 or i == j:
            dp[i][j] = 1

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1

for i in range(2, 31):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k])
