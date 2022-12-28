import sys


k = int(sys.stdin.readline())

arr = []
for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    arr.append(length)

big_square = 0
small_square = 0
idx = 0
for i in range(6):
    square = arr[i] * arr[(i+1) % 6]

    if big_square < square:
        big_square = square
        idx = i

small_square = arr[(idx+3) % 6] * arr[(idx+4) % 6]
print(k * (big_square - small_square))
