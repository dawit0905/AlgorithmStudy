import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(1001)]
for i in range(0, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][0]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

total = 0
for i in range(1, n+1):
    total += sum(dp[i])

print(sum(dp[n]) % 10007)

