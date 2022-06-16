import sys

for i in range(3):
    total = 0
    n = int(sys.stdin.readline())
    for j in range(n):
        num = int(sys.stdin.readline())
        total += num

    if total < 0:
        print('-')
    elif total > 0:
        print('+')
    else:
        print('0')
