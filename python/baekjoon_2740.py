import sys

n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n2, m2 = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n2)]
C = [[0] * m2 for _ in range(n)]

for i in range(n):
    for j in range(m2):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for i in C:
    print(*i)