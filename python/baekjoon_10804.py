import sys


arr = [i for i in range(0, 21)]

for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    tmp = arr[a:b+1]
    len = b-a
    for i in range(len+1):
        arr[a+i] = tmp[len-i]


print(*arr[1:])
