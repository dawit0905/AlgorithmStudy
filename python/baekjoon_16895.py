import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
grundy = 0
cnt = 0

for i in arr:
    grundy ^= i

for i in range(n):
    for j in range(1, arr[i]+1):
        temp = arr[i] - j
        temp ^= arr[i]
        temp ^= grundy
        if temp == 0:
            cnt += 1

print(cnt)
