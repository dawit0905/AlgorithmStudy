import sys

while 1:
    arr = list(map(int, sys.stdin.readline().rstrip()))
    if arr[0] == 0:
        exit(0)

    length = len(arr) - 1
    flag = 1
    for i in range(length+1):
        if arr[i] != arr[length-i]:
            flag = 0
            break
    if flag:
        print('yes')
    else:
        print('no')