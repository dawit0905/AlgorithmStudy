import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if n <= k:
    print(0)
    exit(0)
else:
    arr.sort()
    diff_arr = []
    for i in range(len(arr)-1):
        diff_arr.append(abs(arr[i]-arr[i+1]))

    diff_arr.sort()

    # print(diff_arr[:n-k])
    print(sum(diff_arr[:n-k]))
