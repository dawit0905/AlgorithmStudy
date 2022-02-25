import sys


def recursion(x, y, n):
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                recursion(x, y, n // 2)
                recursion(x, y + n // 2, n // 2)
                recursion(x + n // 2, y, n // 2)
                recursion(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1


n = int(sys.stdin.readline())
arr = []
result = [0, 0]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
recursion(0, 0, n)

print(result[0])
print(result[1])
