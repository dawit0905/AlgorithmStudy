import sys


def mul(n, matrix, matrix2) -> list:
    matrix3 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix3[i][j] += matrix[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000
    return matrix3


def devide(n, k, matrix):
    if k == 1:
        return matrix
    elif k == 2:
        return mul(n, matrix, matrix)
    else:
        tmp = devide(n, k//2, matrix)
        if k % 2 == 0:
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), matrix)


n, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = devide(n, k, matrix)

for i in answer:
    for j in i:
        print(j%1000, end=" ")
    print()
