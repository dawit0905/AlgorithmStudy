import sys

n, k = map(int, sys.stdin.readline().split())
dp = [100001] * (k+1)
dp[0] = 0

for i in range(n):
    coin = int(sys.stdin.readline())
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
