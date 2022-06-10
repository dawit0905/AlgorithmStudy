import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    arr = []
    cnt = 1

    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr = sorted(arr)
    check = arr[0][1]

    for i in range(1, n):
        if check > arr[i][1]:
            check = arr[i][1]
            cnt += 1

print(cnt)