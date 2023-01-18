import sys


tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(sum(arr))

