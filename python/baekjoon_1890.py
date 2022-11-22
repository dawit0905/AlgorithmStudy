import sys


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if i == n-1 and j == n-1:
            print(dp[i][j])
            break

        if j + arr[i][j] < n:
            dp[i][j+arr[i][j]] += dp[i][j]

        if i + arr[i][j] < n:
            dp[i+arr[i][j]][j] += dp[i][j]

