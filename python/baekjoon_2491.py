import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp_up = [0] * (n+1)
dp_down = [0] * (n+1)


for i in range(1, n):
    # dp_up
    if arr[i-1] <= arr[i]:
        dp_up[i] += dp_up[i-1] + 1
    # dp _down
    if arr[i-1] >= arr[i]:
        dp_down[i] += dp_down[i-1] + 1

print(max(max(dp_up), max(dp_down)) + 1)
