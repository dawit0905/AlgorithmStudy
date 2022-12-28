import sys


def make_four(size) -> list:
    number = 1
    count = size // 4
    arr = [[0] * size for _ in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            arr[i][j] = number
            number += 1
    for row in range(0, count):
        col1 = size // 4
        col2 = size - size // 4 - 1
        for i in range(0, size // 2):
            arr[row][col1], arr[size - 1 - row][col2] = arr[size - 1 - row][col2], arr[row][col1]
            arr[col1][row], arr[col2][size - 1 - row] = arr[col2][size - 1 - row], arr[col1][row]
            col1 += 1
            col2 -= 1

    return arr


def make_even(size):
    tsize = n // 2
    qua = n // 4
    val = n * n // 4
    arr = [[0] * size for _ in range(size)]
    tmp = make_odd(tsize)

    for i in range(tsize):
        for j in range(tsize):
            if j < qua:
                arr[i][j] = 3 * val
    arr[qua][0] = 0
    arr[qua][qua] = 3 * val

    for i in range(tsize, n):
        for j in range(tsize):
            if arr[i - tsize][j] == 0:
                arr[i][j] = 3 * val

    for i in range(tsize):
        for j in range(tsize, n):
            arr[i][j] = val if n - qua < j else 2 * val

    for i in range(tsize, n):
        for j in range(tsize, n):
            arr[i][j] = 2 * val if arr[i - tsize][j] == val else val

    for dx, dy in [(0, 0), (0, tsize), (tsize, 0), (tsize, tsize)]:
        for i in range(tsize):
            for j in range(tsize):
                arr[i + dx][j + dy] += tmp[i][j]

    return arr


def make_odd(size) -> list:
    row = 0
    col = size // 2
    arr = [[0] * size for _ in range(size)]

    for number in range(1, size * size + 1):
        arr[row][col] = number
        if number % size == 0:
            row += 1
        else:
            row -= 1
            col += 1
            if row < 0:
                row = size - 1
            if col > size - 1:
                col = 0
    return arr


def print_mbj(size):
    for i in range(size):
        for j in range(size):
            print(answer[i][j], end=" ")
        print()


n = int(sys.stdin.readline())

if n % 2 == 0:
    if n % 4 == 0:
        answer = make_four(n)
    else:
        answer = make_even(n)
else:
    answer = make_odd(n)

print_mbj(n)
