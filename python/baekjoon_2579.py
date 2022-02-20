import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0] * n

for i in range(n):
    if i == 0 :
        dp[i] = arr[i]
        continue
    elif i == 1:
        dp[i] = arr[0] + arr[i]
        continue
    elif i == 2:
        dp[i] = max(arr[0],arr[1]) + arr[2]
        continue
    dp[i] = max(dp[i-3]+arr[i-1],dp[i-2]) + arr[i]

print(dp[-1])
