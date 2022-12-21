import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]


m = int(sys.stdin.readline())
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if a == 0:
        print(prefix_sum[b])
    else:
        print(prefix_sum[b] - prefix_sum[a-1])
