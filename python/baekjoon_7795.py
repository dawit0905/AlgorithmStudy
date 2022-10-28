import sys


def binary_search(arr, num):

    left = 0
    right = len(arr)-1
    result = -1
    while left <= right:
        mid = (left+right) // 2

        if arr[mid] < num:
            result = mid
            left = mid+1
        else:
            right = mid-1

    return result


t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()

    answer = 0
    for a in A:
        answer += binary_search(B, a)+1

    print(answer)
