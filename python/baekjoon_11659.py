import sys

n, t = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr_sum = [0 for i in range(n)]
arr_sum[0] = arr[0]

for i in range(1, len(arr)):
    arr_sum[i] = arr_sum[i-1] + arr[i]

for k in range(t):
    i, j = map(int, sys.stdin.readline().split())

    if i == 1:
        print(arr_sum[j - 1])
    else:
        print(arr_sum[j-1] - arr_sum[i-2])
