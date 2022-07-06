import sys

for i in range(3):
    arr = list(map(int, sys.stdin.readline().split()))

    total = sum(arr)
    if total == 3:
        print('A')
    elif total == 2:
        print('B')
    elif total == 1:
        print('C')
    elif total == 0:
        print('D')
    elif total == 4:
        print('E')