import sys
import math
k, n = map(int, sys.stdin.readline().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)
result = []
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        total = total + (i // mid)

    if n > total:
        end = mid - 1
        result.append(end)
    else :
        start = mid + 1

print(end)
print(result)