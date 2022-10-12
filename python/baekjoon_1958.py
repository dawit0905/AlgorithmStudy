import sys


a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()

len_a = len(a)
len_b = len(b)
len_c = len(c)

dp = [[[0] * (len_c+1) for _ in range(len_b+1)] for __ in range(len_a+1)]

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        for t in range(1, len_c+1):
            if a[i-1] == b[j-1] and b[j-1] == c[t-1]:
                dp[i][j][t] = dp[i-1][j-1][t-1] + 1
            else:
                dp[i][j][t] = max(dp[i-1][j][t], dp[i][j-1][t], dp[i][j][t-1])

print(dp[-1][-1][-1])
