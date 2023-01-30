import sys


n = int(sys.stdin.readline())
A, B = 100, 100

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        B -= a
    elif a < b:
        A -= b

print(A)
print(B)
