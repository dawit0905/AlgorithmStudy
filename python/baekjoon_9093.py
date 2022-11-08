import sys


n = int(sys.stdin.readline())

for _ in range(n):
    arr = sys.stdin.readline().rstrip().split()
    for i in range(len(arr)):
        for j in range(len(arr[i])-1, -1, -1):
            print(arr[i][j], end="")
        print(end=" ")
    print()
