n = int(input())

for i in range(n):
    for k in range(i):
        print(' ', end="")

    for j in range(n, 0+i, -1):
        print('*', end="")
    print()