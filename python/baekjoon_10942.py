import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for start in range(n-i):
        end = start + i

        if start == end:
            dp[start][end] = 1
        elif arr[start] == arr[end]:
            if start+1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
