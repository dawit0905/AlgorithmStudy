import sys


def mergesort(left, right):
    if left == right:
        return

    mid = (left+right)//2
    mergesort(left, mid)
    mergesort(mid+1, right)
    merge(left, right)


def merge(left, right):
    if ((right - left) > (n / k)):  ##정렬 정지 조건
        return
    mid = int((left + right) / 2)
    idx1 = left
    idx2 = mid + 1
    idx3 = 0

    while (idx1 <= mid and idx2 <= right):
        if (arr[idx1] <= arr[idx2]):
            tmp[idx3] = arr[idx1]
            idx3 += 1
            idx1 += 1
        else:
            tmp[idx3] = arr[idx2]
            idx3 += 1
            idx2 += 1
    while (idx1 <= mid):
        tmp[idx3] = arr[idx1]
        idx3 += 1
        idx1 += 1
    while (idx2 <= right):
        tmp[idx3] = arr[idx2]
        idx3 += 1
        idx2 += 1

    for i in range(left, right + 1):
        arr[i] = tmp[i - left]


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
tmp = [0] * n

mergesort(0, n-1)
print(*arr)
