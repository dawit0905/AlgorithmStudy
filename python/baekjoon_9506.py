import sys


while True:
    num = int(sys.stdin.readline())

    if num == -1:
        break

    total = 0
    num_list = []
    for i in range(1, num):
        if num % i == 0:
            total += i
            num_list.append(i)

    if num == total:
        print(f'{num} = ', end='')
        print(*num_list, sep=' + ')
    else:
        print(f'{num} is NOT perfect.')
