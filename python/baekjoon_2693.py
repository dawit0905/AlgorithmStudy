import sys


tc = int(sys.stdin.readline())

for t in range(tc):
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(2):
        arr.remove(max(arr))

    print(max(arr))
