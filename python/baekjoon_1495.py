import sys


n, s, m = map(int, sys.stdin.readline().split())
volumn = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j+volumn[i] <= m:
                dp[i+1][j+volumn[i]] = 1
            if j-volumn[i] >= 0:
                dp[i+1][j-volumn[i]] = 1

ans = -1
for i in range(m, -1, -1):
    if dp[n][i]==1:
        ans = i
        break

print(ans)


'''
3 5 10
5 3 7

0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1

dp[n][i] == 1
'''