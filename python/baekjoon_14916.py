import sys


n = int(sys.stdin.readline())
dp = [sys.maxsize] * (100001)
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[n]) if dp[n] != sys.maxsize else print(-1)
