import sys


tc = int(sys.stdin.readline())

for t in range(tc):
    arr = list(map(int, sys.stdin.readline().split()))

    arr.remove(max(arr))
    arr.remove(min(arr))


    if max(arr) - min(arr) >= 4:
        print('KIN')
    else:
        print(sum(arr))
