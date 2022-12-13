import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline()))

    b = []
    for j in range(m):
        b.append(int(sys.stdin.readline()))

    cnt = 0
    for num in a:
        start = 0
        end = m
        while start <= end:
            mid = (start+end)//2

            if b[mid] == num:
                cnt += 1
                break
            elif b[mid] > num:
                end = mid-1
            else:
                start = mid+1

    print(cnt)

