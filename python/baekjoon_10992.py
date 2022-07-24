import sys

n = int(sys.stdin.readline())

for i in range(n):
    for k in range(n-i-1):
        print(' ', end='')

    for j in range(i*2+1):
        if i > 0 and i < n-1 and 1 <= j <= i*2-1 :
            print(' ', end='')
        else:
            print('*', end='')

    print()
