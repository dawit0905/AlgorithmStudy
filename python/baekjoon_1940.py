import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
start = 0
end = len(arr)-1

cnt = 0
while start < end:
    num = arr[start] + arr[end]

    if num == m:
        cnt += 1
        start += 1
        end -= 1
    elif num < m:
        start += 1
    else:
        end -= 1

print(cnt)
