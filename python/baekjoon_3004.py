import sys


n, w, h = map(int, sys.stdin.readline().split())

for i in range(n):
    a = int(sys.stdin.readline())

    if a ** 2 <= w ** 2 + h ** 2:
        print('DA')
    else:
        print('NE')

