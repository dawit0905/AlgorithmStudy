import sys


def mergesort(start, end):
    global cnt
    if start < end:
        mid = (start+end) // 2

        mergesort(start, mid)
        mergesort(mid+1, end)

        a = start
        b = mid+1
        tmp = []

        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1
            else:
                tmp.append(arr[b])
                b += 1
                cnt += mid-a+1

        if a <= mid:
            tmp = tmp + arr[a:mid+1]
        if b <= end:
            tmp = tmp + arr[b:end+1]

        for i in range(len(tmp)):
            arr[start+i] = tmp[i]


sys.setrecursionlimit(int(10**5))
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
mergesort(0, n-1)

print(cnt)


