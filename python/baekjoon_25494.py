import sys


t = int(sys.stdin.readline())

for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))

    answer = min(arr)
    print(answer)