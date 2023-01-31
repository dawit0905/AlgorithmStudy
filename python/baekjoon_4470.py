import sys


n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in range(1, n+1):
    print(f'{i}. {arr[i-1]}')