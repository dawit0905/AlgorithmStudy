import sys

total = int(sys.stdin.readline())
arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

print(total-sum(arr))