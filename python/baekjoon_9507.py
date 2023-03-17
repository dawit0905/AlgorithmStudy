import sys


tc = int(sys.stdin.readline())
dp = [0] * 70
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 8

for i in range(5, 70):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

for t in range(tc):
    n = int(sys.stdin.readline())
    print(dp[n])
