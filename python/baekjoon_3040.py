import sys


def sol():
    total = sum(arr)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if total - (arr[i] + arr[j]) == 100:
                return [i, j]


arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

a, b = sol()

for i in range(9):
    if i != a and i != b:
        print(arr[i])
