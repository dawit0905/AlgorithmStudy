import sys


s = sys.stdin.readline().strip()
n = len(s)
dp = [[0] * n for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 0

for i in range(1, n):
    if 10 <= int(s[i-1:i+1]) <= 34:
        dp[1][i] = dp[0][i-1]

    if s[i] == '0':
        continue

    dp[0][i] = dp[0][i-1] + dp[1][i-1]

print(int(dp[0][n-1] + int(dp[1][n-1])))
