import sys


a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())


if a+b < c * 2:
    print(a+b)
else:
    print(a+b - (c*2))
