import sys


n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]

answer = []
while len(arr):
    answer.append(arr.pop(0))
    if len(arr):
        arr.append(arr.pop(0))

print(*answer)
