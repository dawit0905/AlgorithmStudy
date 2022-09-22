import sys


n = int(sys.stdin.readline())
arr = []
INF = sys.maxsize
ans = INF

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for color in range(3):
    dp = [[0] * 3 for __ in range(n)]

    for j in range(3):
        if j == color:
            dp[0][j] = arr[0][j]
        else:
            dp[0][j] = INF

    for i in range(1, n):
        dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i != color:
            ans = min(ans, dp[-1][i])

print(ans)
