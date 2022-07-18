import sys


n = int(sys.stdin.readline())

for i in range(1, n+1):

    print(' '*(n-i), end="")

    for j in range(i*2-1):
        if j%2 == 1:
            print(' ', end="")
        else:
            print('*', end="")
    print()
