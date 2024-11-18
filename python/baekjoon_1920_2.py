import sys


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
A.sort()

for num in M:
    flag = 0
    start = 0
    end = n-1
    while start <= end and flag == 0:
        mid = (start+end)//2

        if A[mid] == num:
            flag = 1
        elif A[mid] < num:
            start = mid + 1
        else:
            end = mid -1

    print(1) if flag else print(0)
