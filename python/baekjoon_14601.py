import sys


def check(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != 0:
                return False
    return True


def recur(x, y, size):
    global cnt
    cnt += 1

    halfSize = size // 2
    if check(x, y, halfSize):
        arr[x+halfSize-1][y+halfSize-1] = cnt
    if check(x, y+halfSize, halfSize):
        arr[x+halfSize-1][y+halfSize] = cnt
    if check(x+halfSize, y, halfSize):
        arr[x+halfSize][y+halfSize-1] = cnt
    if check(x+halfSize, y+halfSize, halfSize):
        arr[x+halfSize][y+halfSize] = cnt

    if size == 2:
        return

    recur(x, y, halfSize)
    recur(x+halfSize, y, halfSize)
    recur(x, y+halfSize, halfSize)
    recur(x+halfSize, y+halfSize, halfSize)


k = int(sys.stdin.readline())
y, x = map(int, sys.stdin.readline().split())
arr = [[0] * (2**k) for _ in range((2**k))]
cnt = 0

x = (1<<k) - x
y = y - 1
arr[x][y] = -1

recur(0, 0, (1<<k))

for i in arr:
    print(*i)

