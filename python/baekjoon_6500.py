import sys


while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break

    arr = []

    while True:
        n = str(int(n) ** 2)

        while len(n) < 8:
            n = '0' + n

        if n in arr:
            break

        arr.append(n)

        n = n[2:6]

    print(len(arr))
