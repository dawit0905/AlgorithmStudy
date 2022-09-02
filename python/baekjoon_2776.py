import sys


t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    arr = set(list(map(int, sys.stdin.readline().split())))

    m = int(sys.stdin.readline())
    arr2 = list(map(int, sys.stdin.readline().split()))

    for i in arr2:
        if i in arr:
            print(1)
        else:
            print(0)
