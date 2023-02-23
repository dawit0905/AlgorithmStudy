import sys


n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    for j in range(b):
        print('X'*a)

    print()