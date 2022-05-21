import sys

'''
1 2 3
'''
dp = [0] * 1000001
n = int(sys.stdin.readline())
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n])