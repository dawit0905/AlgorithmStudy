import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
max_num = max(dp)
arr2 = []
for i in range(n-1, -1, -1):
    if dp[i] == max_num:
        arr2.append(arr[i])
        max_num -= 1
arr2.reverse()
print(*arr2)
