import sys


k = int(sys.stdin.readline())

for i in range(1, k+1):
    n, *arr = map(int, sys.stdin.readline().split())

    arr = list(arr)
    print(f"Class {i}")
    max_num = max(arr)
    min_num = min(arr)
    arr.sort()
    gap = 0

    for i in range(n-1):
        gap = max(gap, arr[i+1] - arr[i])

    print(f"Max {max_num}, Min {min_num}, Largest gap {gap}")
