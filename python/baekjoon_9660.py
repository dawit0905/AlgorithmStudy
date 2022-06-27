import sys

arr = [0, 1, 0, 1, 1, 1, 1]

n = int(sys.stdin.readline())

if arr[n%7] == 1:
    print('SK')
else:
    print('CY')