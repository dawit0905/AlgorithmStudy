import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

num = 1
arr = []

while num**2 <= n:
    temp = num**2
    if temp >= m:
        arr.append(temp)

    num += 1

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
