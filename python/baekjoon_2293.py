import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    coin.append(int(sys.stdin.readline()))

for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = dp[j] + dp[j - coin[i]]

print(dp[k])
# print(dp)
# print(coin)