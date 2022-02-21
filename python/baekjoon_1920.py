import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
n_arr.sort()
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

for i in m_arr:
    start = 0
    end = n-1
    flag = 0
    while start <= end:
        mid = (start+end) // 2
        if n_arr[mid] == i:
            flag = 1
            break
        elif i < n_arr[mid]:
            end = mid - 1
        else :
            start = mid + 1
    print(flag)