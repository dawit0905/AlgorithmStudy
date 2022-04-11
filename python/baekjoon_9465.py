import sys

t = int(sys.stdin.readline())

for _ in range(t):
    arr = []
    n = int(sys.stdin.readline())
    dp = [[0] * n for _ in range(2)]
    for _ in range(2):
        arr.append(list(map(int, sys.stdin.readline().split())))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    for i in range(1, n):
        for j in range(2):
            if j==0:
                dp[j][i] = max(arr[j][i]+dp[j+1][i-1], dp[j][i-1])
            elif j==1:
                dp[j][i] = max(arr[j][i]+dp[j-1][i-1], dp[j][i-1])

    print(max(dp[0][n-1],dp[1][n-1]))
