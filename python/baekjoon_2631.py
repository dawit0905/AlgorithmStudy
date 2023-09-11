import sys


n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

dp = [1] * n
for k in range(1, n):
    for i in range(0, k):
        if arr[i] < arr[k]:
            dp[k] = max(dp[k], dp[i] + 1)

print(n - max(dp))
