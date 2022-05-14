import sys

n = int(sys.stdin.readline())
min_dp = [[0] * 3 for _ in range(n)]
max_dp = [[0] * 3 for _ in range(n)]
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(data[0])):
    min_dp[0][i] = data[0][i]
    max_dp[0][i] = data[0][i]
for i in range(1, n):
    for j in range(3):

        if j == 0:
            min_dp[i][j] = min(min_dp[i-1][j], min_dp[i-1][j+1]) + data[i][j]
            max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i - 1][j + 1]) + data[i][j]
        elif j == n-1:
            min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i-1][j]) + data[i][j]
            max_dp[i][j] = max(max_dp[i-1][j-1], max_dp[i-1][j]) + data[i][j]
        else:
            min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i-1][j], min_dp[i-1][j+1]) + data[i][j]
            max_dp[i][j] = max(max_dp[i-1][j-1], max_dp[i-1][j], max_dp[i-1][j+1]) + data[i][j]

print(max(max_dp[-1]), min(min_dp[-1]))
