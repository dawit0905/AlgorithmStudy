import sys


n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

start = 0
end = min(arr) * m
result = 0

while start <= end:
    mid = (start+end)//2
    temp = 0
    for i in arr:
        temp += mid//i

    if temp >= m:
        end = mid-1
        result = mid
    else:
        start = mid + 1

print(result)

