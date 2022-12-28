import sys


while 1:
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print('right')
        else:
            print('wrong')
