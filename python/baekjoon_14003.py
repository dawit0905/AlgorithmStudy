import sys
from bisect import bisect_left


n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
cmp = [-1000000001]
max_num = 0

for i in range(1, n+1):
    if cmp[-1] < arr[i]:
        cmp.append(arr[i])
        dp[i] = len(cmp) - 1
        max_num = dp[i]
    else:
        dp[i] = bisect_left(cmp, arr[i])
        cmp[dp[i]] = arr[i]

print(max_num)

res = []
for i in range(n, 0, -1):
    if dp[i] == max_num:
        res.append(arr[i])
        max_num -= 1
res.reverse()
print(*res)
