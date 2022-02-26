from math import inf

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    min_num = inf
    j = 1

    while (j**2) <= i:
        min_num = min(min_num, dp[i - (j**2)])
        j += 1

    dp.append(min_num+1)

print(dp[n])