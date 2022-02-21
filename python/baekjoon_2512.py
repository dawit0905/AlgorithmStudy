import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(arr)
result = 0

while start <= end:
    mid = (start+end) // 2
    total = 0

    for i in arr:

        if i > mid:
            total += mid
        else:
            total += i

    if total <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)