import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    elif total >= m:
        start = mid + 1
        result = mid

print(result)