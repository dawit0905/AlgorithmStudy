import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')
