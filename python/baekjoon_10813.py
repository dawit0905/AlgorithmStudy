import sys


n, m = map(int, sys.stdin.readline().split())
arr = [i+1 for i in range(0, n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    arr[a], arr[b] = arr[b], arr[a]

print(*arr)