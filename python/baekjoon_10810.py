import sys


n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n+1)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(a, b+1):
        arr[j] = c

print(*arr[1:])