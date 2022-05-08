import sys

n, m, k = map(int, sys.stdin.readline().split())

if n*m < k:
    print(0)
else:
    print(n*m - k)