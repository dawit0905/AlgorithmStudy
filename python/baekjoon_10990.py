import sys


n = int(sys.stdin.readline())

for i in range(1, n+1):
    print((n - i) * ' ', end="")
    if i == 1:
        print('*')
    else:
        print('*', end="")
        print(((i*2)-3) * ' ', end="")
        print('*')