n = int(input())

dp = [1, 1, 1, 2, 2] + [0] * 96

for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for i in range(n):
    p = int(input())
    print(dp[p - 1])
# print(len(dp))
