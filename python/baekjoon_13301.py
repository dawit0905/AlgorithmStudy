import sys

# row column
# 1 1 4
# 2 1 6
# 2 3 10
# 5 3 16
# 5 8 26

n = int(sys.stdin.readline())

dp = [[0,0] for _ in range(81)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n+1):
    if i % 2:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][1]

print(dp[n][0] * 2 + dp[n][1] * 2)
