import sys


n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)
for i in arr:
    print(i)
