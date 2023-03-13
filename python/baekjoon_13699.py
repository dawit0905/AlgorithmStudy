import sys


def t(n):
    if n == 0:
        return 1
    if not dp[n]:
        for i in range(n):
            dp[n] += t(i) * t(n-1-i)
    return dp[n]


n = int(sys.stdin.readline())
dp = [0]*36
print(t(n))
